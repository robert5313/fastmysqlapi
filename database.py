from peewee import *

user = 'root'
password = ''
db_name = 'fastapi_contact'

conn = MySQLDatabase(
    db_name, user=user,
    password=password,
    host='localhost'
)

class BaseModel(Model):
    class Meta:
        database = conn