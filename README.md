# MySQL透视器(MySQL Inspector)

## 透视效果如下

# 数据表

|    |        |                    |                                                                         |    |        |                     |
| -- | ------ | ------------------ | ----------------------------------------------------------------------- | -- | ------ | ------------------- |
| 1  | alpha  | user               | [user](/database/schemas/alpha/tables/user)                             |    | 0      | 2018-12-30 16:20:02 |
| 2  | beta   | bj\_animal         | [bj\_animal](/database/schemas/beta/tables/bj_animal)                   |    | 0      | 2018-12-30 16:20:02 |
| 3  | beta   | fl\_plant          | [fl\_plant](/database/schemas/beta/tables/fl_plant)                     |    | 0      | 2018-12-30 16:20:02 |
| 4  | camera | video\_recognition | [video\_recognition](/database/schemas/camera/tables/video_recognition) |    | 0      | 2018-12-30 16:19:12 |
| 5  | camera | video\_segment     | [video\_segment](/database/schemas/camera/tables/video_segment)         |    | 0      | 2018-12-30 16:19:12 |
| 6  | poem   | hello              | [hello](/database/schemas/poem/tables/hello)                            |    | 15     | 2018-12-31 23:24:37 |
| 7  | poem   | poem               | [poem](/database/schemas/poem/tables/poem)                              | 诗歌 | 6565   | 2019-02-22 16:19:01 |
| 8  | poem   | poem\_part         | [poem\_part](/database/schemas/poem/tables/poem_part)                   |    | 123614 | 2018-12-31 19:50:57 |
| 9  | poem   | poem\_tag          | [poem\_tag](/database/schemas/poem/tables/poem_tag)                     |    | 228    | 2019-01-01 00:44:31 |
| 10 | poem   | sentence           | [sentence](/database/schemas/poem/tables/sentence)                      |    | 8387   | 2018-12-31 17:50:27 |
| 11 | poem   | sentence\_part     | [sentence\_part](/database/schemas/poem/tables/sentence_part)           |    | 20558  | 2018-12-31 17:50:27 |

# 表信息

|            |                     |
| ---------- | ------------------- |
| Name       | poem                |
| Comment    | 诗歌                  |
| Rows       | 6565                |
| Created At | 2019-02-22 16:19:01 |

# 数据列

|          |      |         |
| -------- | ---- | ------- |
| poem\_id | 诗歌ID | int(11) |
| dynasty  | 朝代   | text    |
| author   | 诗人   | text    |
| title    | 标题   | text    |
| content  | 内容   | text    |

# 示例数据

## 示例数据 1

|          |      |                           |
| -------- | ---- | ------------------------- |
| poem\_id | 诗歌ID | 5402                      |
| dynasty  | 朝代   | 唐代                        |
| author   | 诗人   | 虞世南                       |
| title    | 标题   | 蝉                         |
| content  | 内容   | 垂緌饮清露，流响出疏桐。 居高声自远，非是藉秋风。 |

## 示例数据 2

|          |      |                                                                       |
| -------- | ---- | --------------------------------------------------------------------- |
| poem\_id | 诗歌ID | 6313                                                                  |
| dynasty  | 朝代   | 五代                                                                    |
| author   | 诗人   | 顾敻                                                                    |
| title    | 标题   | 河传·棹举                                                                 |
| content  | 内容   | 棹举，舟去，波光渺渺，不知何处？岸花汀草共依依，雨微，鹧鸪相逐飞。 天涯离恨江声咽，啼猿切，此意向谁说？倚兰桡，独无聊，魂消，小炉香欲焦。 |

## 示例数据 3

|          |      |                                                             |
| -------- | ---- | ----------------------------------------------------------- |
| poem\_id | 诗歌ID | 2109                                                        |
| dynasty  | 朝代   | 明代                                                          |
| author   | 诗人   | 刘基                                                          |
| title    | 标题   | 眼儿媚·秋思                                                      |
| content  | 内容   | 萋萋芳草小楼西，云压雁声低。两行疏柳，一丝残照，万点鸦栖。 春山碧树秋重绿，人在武陵溪。无情明月，有情归梦，同到幽闺。 |

## 示例数据 4

|          |      |                           |
| -------- | ---- | ------------------------- |
| poem\_id | 诗歌ID | 5819                      |
| dynasty  | 朝代   | 唐代                        |
| author   | 诗人   | 施肩吾                       |
| title    | 标题   | 瀑布                        |
| content  | 内容   | 豁开青冥颠，泻出万丈泉。 如裁一条素，白日悬秋天。 |

## 示例数据 5

|          |      |                                                       |
| -------- | ---- | ----------------------------------------------------- |
| poem\_id | 诗歌ID | 2871                                                  |
| dynasty  | 朝代   | 清代                                                    |
| author   | 诗人   | 纳兰性德                                                  |
| title    | 标题   | 采桑子·拨灯书尽红笺也                                           |
| content  | 内容   | 拨灯书尽红笺也，依旧无聊。玉漏迢迢，梦里寒花隔玉箫。 几竿修竹三更雨，叶叶萧萧。分付秋潮，莫误双鱼到谢桥。 |
