from models.base_model import BaseModel
import peewee as pw
import re
from werkzeug.security import generate_password_hash
from flask_login import UserMixin
from playhouse.hybrid import hybrid_property

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