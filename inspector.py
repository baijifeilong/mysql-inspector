import os
import random
from argparse import ArgumentParser

import flask
import mysql.connector
from colorlog import logging

os.environ.setdefault("FLASK_ENV", "development")
logging.basicConfig(level='INFO', datefmt='%Y-%m-%d %H:%M:%S',
                    format='%(black)s%(asctime)s.%(msecs)03d %(log_color)s%(levelname)8s%(reset)s %(black)s%(name)-10s %(message)s')
app = flask.Flask(__name__)

parser = ArgumentParser()
parser.add_argument("--host", "-H", default="127.0.0.1", help="Hostname of MySQL")
parser.add_argument("--port", default="3306", help="Port of MySQL")
parser.add_argument("--user", "-u", default="root", help="Username of MySQL")
parser.add_argument("--password", "-p", default="root", help="Password of MySQL")
parser.add_argument("--bind", "-b", default="0.0.0.0", help="Bind network address")
parser.add_argument("--listen", "-l", default="5000", help="Bind port")
args = parser.parse_args()
print(args)
host = args.host
port = args.port
user = args.user
password = args.password
listen = args.listen
bind = args.bind


def connect_mysql():
    return mysql.connector.connect(host=host, port=port, user=user, password=password)


def fetch_tables():
    conn = connect_mysql()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("""
SELECT *
FROM information_schema.TABLES
WHERE TABLE_SCHEMA NOT IN ('mysql', 'sys', 'information_schema', 'performance_schema')
""")
    tables = cursor.fetchall()
    return tables


def fetch_table_info(schema: str, table: str):
    conn = connect_mysql()
    conn.database = "information_schema"
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM information_schema.TABLES WHERE TABLE_SCHEMA = %s AND TABLE_NAME = %s",
                   (schema, table))
    return cursor.fetchone()


def fetch_columns(schema: str, table: str):
    conn = connect_mysql()
    conn.database = "information_schema"
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM information_schema.COLUMNS WHERE TABLE_SCHEMA=%s AND TABLE_NAME=%s", (schema, table))
    columns = cursor.fetchall()
    return columns


def fetch_sample(schema: str, table: str):
    info = fetch_table_info(schema, table)
    columns = fetch_columns(schema, table)
    primary_column = next(filter(lambda x: x["COLUMN_KEY"] == "PRI", columns), None)
    primary_key = primary_column["COLUMN_NAME"] if primary_column else None
    primary_key_is_integer = 'int' in primary_column["COLUMN_TYPE"] if primary_column else False
    conn = connect_mysql()
    conn.database = schema
    cursor = conn.cursor(dictionary=True)
    if primary_key_is_integer:
        cursor.execute("""
SELECT `{0}`.*
FROM `{0}`
       JOIN (SELECT RAND() * MAX({1}) AS {1} FROM `{0}`) AS random ON {0}.{1} > random.{1}
LIMIT 1;
    """.format(table, primary_key))
    elif info["TABLE_ROWS"] < 10000:
        cursor.execute("SELECT * FROM {} ORDER BY RAND() LIMIT 1".format(table))
    elif primary_key:
        cursor.execute("SELECT * FROM {} ORDER BY {} DESC LIMIT 100".format(table, primary_key))
    else:
        cursor.execute("SELECT * FROM {} LIMIT 100".format(table))
    samples = cursor.fetchall()
    return random.choice(samples) if samples else None


def fetch_samples(schema: str, table: str):
    samples = [fetch_sample(schema, table) for _ in range(5)]
    samples = [dict(x) for x in {tuple(y.items()) for y in samples if y}]
    return samples


@app.route("/")
def query_tables():
    tables = fetch_tables()
    return flask.render_template("tables.html", tables=tables)


@app.route("/schemas/<string:schema>/tables/<string:table>")
def show_table(schema: str, table: str):
    tables = fetch_tables()
    info = next(filter(lambda x: x["TABLE_SCHEMA"] == schema and x["TABLE_NAME"] == table, tables))
    columns = fetch_columns(schema=schema, table=table)
    column_dict = dict((x["COLUMN_NAME"], x) for x in columns)
    samples = fetch_samples(schema=schema, table=table)
    return flask.render_template("table.html", columns=columns, info=info, samples=samples,
                                 column_dict=column_dict)


connect_mysql()
app.run(host=bind, port=listen)
