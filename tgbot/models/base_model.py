from peewee import MySQLDatabase, Model

db = MySQLDatabase(database='demo', host='test.cg45.xyz', port=31008, user='root', password='c60AWBnmitRY0Gst')


# db.init(
#     database='demo',
#     host='test.cg45.xyz',
#     port=31008,
#     user='root',
#     password='c60AWBnmitRY0Gst',
#     autocommit=True
# )

class BaseModel(Model):
    """
    基础 实体类基础
    """

    class Meta:
        database = db
