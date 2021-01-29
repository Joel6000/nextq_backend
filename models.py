import os
import peewee as pw
import datetime
from playhouse.postgres_ext import PostgresqlExtDatabase

db = PostgresqlExtDatabase(os.getenv('DATABASE'))

class BaseModel(pw.Model):
    created_at = pw.DateTimeField(default=datetime.datetime.now)
    updated_at = pw.DateTimeField(default=datetime.datetime.now)
    
    def save(self, *args, **kwargs):
        self.updated_at = datetime.datetime.now()
        return super(BaseModel, self).save(*args, *kwargs)

    class Meta:
        database = db
        legacy_table_names = False


class User(BaseModel):
    name = pw.CharField(unique = False, null = False)
    email = pw.CharField(unique=True, null = False)
    password_hash = pw.TextField(null=False)
    password = None
    mobile = pw.CharField(unique=True)

    def validate(self):
        existing_user_email = User.get_or_none(User.email == self.email)
        if existing_user_email and existing_user_email.id != self.id:
            self.errors.append(f"User with {self.email} already exists")

        existing_user_username = User.get_or_none(User.username == self.username)
        if existing_user_username and existing_user_username.id != self.id:
            self.errors.append(f"User with {self.username} already exists.")

        #Passwords
        if self.password:
            if len(self.password) <= 6:
                self.errors.append(f"Password must at least have six characters")

            has_lower = re.search(r"[a-z]", self.password)
            has_upper = re.search(r"[A-Z]",self.password)
            has_special = re.search(r"[\[ \] \@ \$ \* \^ \# \%]", self.password)

            if has_lower and has_upper and has_special:
                self.password_hash = generate_password_hash(self.password)
            else:
                self.errors.append(f"Password requires changes")


class Store(BaseModel):
    name = pw.CharField()
    location = pw.CharField()
    customer_limit = pw.IntegerField(null=True)

class History(BaseModel):
    user = pw.ForeignKeyField(User)
    store = pw.ForeignKeyField(Store)
    time_in = pw.DateTimeField(default=datetime.datetime.now)
    time_out = pw.DateTimeField(default=None)

class Queue(BaseModel):
    user = pw.ForeignKeyField(User)
    store = pw.ForeignKeyField(Store)
    queue_time = pw.DateTimeField(default=datetime.datetime.now)