import flask
from colorlog import logging

import database

logging.basicConfig(level='INFO', datefmt='%Y-%m-%d %H:%M:%S',
                    format='%(black)s%(asctime)s.%(msecs)03d %(log_color)s%(levelname)8s%(reset)s %(black)s%(name)-10s %(message)s')
app = flask.Flask(__name__)
app.register_blueprint(database.app)


@app.route("/")
def home():
    return flask.redirect("/database")


app.run()
