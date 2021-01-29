from models.base_model import BaseModel
from models.user import User
from models.store import Store
import datetime
import peewee as pw

class Queue(BaseModel):
    user = pw.ForeignKeyField(User)
    store = pw.ForeignKeyField(Store)
    queue_time = pw.DateTimeField(default=datetime.datetime.now)