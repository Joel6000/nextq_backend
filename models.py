import os
import peewee as pw
import datetime
from playhouse.postgres_ext import PostgresqlExtDatabase


contacts_db = SqliteDatabase('contacts.db')

db = PostgresqlExtDatabase(os.getenv('DATABASE'))

class Base(pw.Model):
    created_at = pw.DateTimeField(default=datetime.datetime.now)
    updated_at = pw.DateTimeField(default=datetime.datetime.now)
    
    def save(self, *args, **kwargs):
        self.updated_at = datetime.datetime.now()
        return super(BaseModel, self).save(*args, *kwargs)

    class Meta:
        database = db
        legacy_table_names = False


class User(Base):
    name = pw.CharField()
    age = pw.IntegerField()
    mobile = pw.IntegerField(unique=True)

class Store(Base):
    name = pw.CharField()
    location = pw.CharField()
    customer_limit = pw.IntegerField(null=True)

class History(Base):
    user = pw.ForeignKeyField(User)
    store = pw.ForeignKeyField(Store)
    time_in = pw.DateTimeField(default=datetime.datetime.now)
    time_out = pw.DateTimeField(default=None)

class Queue(Base):
    user = pw.ForeignKeyField(User)
    store = pw.ForeignKeyField(Store)
    queue_time = pw.DateTimeField(default=datetime.datetime.now)