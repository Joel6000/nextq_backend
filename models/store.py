from models.base_model import BaseModel
import peewee as pw


class Store(BaseModel):
    name = pw.CharField()
    location = pw.CharField()
    customer_limit = pw.IntegerField(null=True) #set default == 10
    headcount = pw.IntegerField(default = 0)
    queue = pw.IntegerField(default = 0)
    image_url = pw.TextField(null=True, default = "https://static.thenounproject.com/png/1369734-200.png" )
