from datetime import datetime
from mongoengine import (
    Document,
    IntField,
    ListField,
    FloatField,
    StringField,
    DateTimeField
)


class LoginOTP(Document):
    otp = IntField()
    user_email = StringField()
    expiry_time = FloatField()
    createdAt = DateTimeField(default=datetime.now)
    updatedAt = DateTimeField(default=datetime.now)

    meta = {"collection": "login_otp"}


class Users(Document):
    user_name = StringField()
    pan_card = StringField()
    client_id = StringField()
    upi_id = StringField()
    type = StringField()
    createdAt = DateTimeField(default=datetime.now)
    updatedAt = DateTimeField(default=datetime.now)


class IPOProviders(Document):
    provider_name = StringField()
    provider_source = ListField()
    createdAt = DateTimeField(default=datetime.now)
    updatedAt = DateTimeField(default=datetime.now)

    meta = {"collection": "ipo_providers"}


class IPONames(Document):
    ipo_name = StringField()
    ipo_provider = StringField()
    createdAt = DateTimeField(default=datetime.now)
    updatedAt = DateTimeField(default=datetime.now)

    meta = {"collection": "ipo_names"}
