from models.base_model import BaseModel
from models.user import User
from models.store import Store
import datetime
import peewee as pw

class Queue(BaseModel):
    user = pw.ForeignKeyField(User,on_delete="CASCADE")
    store = pw.ForeignKeyField(Store,on_delete="CASCADE")
    queue_time = pw.DateTimeField(default=datetime.datetime.now)