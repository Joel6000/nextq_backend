from models.base_model import BaseModel
import peewee as pw


class Store(BaseModel):
    name = pw.CharField()
    location = pw.CharField()
    customer_limit = pw.IntegerField(null=True)
