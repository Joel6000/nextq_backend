from models.base_model import BaseModel
from models.user import User
from models.store import Store
import datetime
import peewee as pw

class History(BaseModel):
    user = pw.ForeignKeyField(User)
    store = pw.ForeignKeyField(Store)
    time_in = pw.DateTimeField(default=datetime.datetime.now)
    time_out = pw.DateTimeField(default=None, null=True)
