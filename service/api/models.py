# Copyright (c) 2023 RFull Development
# This source code is managed under the MIT license. See LICENSE in the project root.
from django.db.models import CASCADE, CharField, ForeignKey, Model
from django.forms import IntegerField


class UserModel(Model):
    name = CharField(max_length=32, unique=True)
    password = CharField(max_length=64)

    def __str__(self) -> str:
        return self.name


class ItemModel(Model):
    name = CharField(max_length=32)
    price = IntegerField()
    code = CharField(max_length=32, unique=True)
    user_id = ForeignKey(UserModel, on_delete=CASCADE)

    def __str__(self) -> str:
        return self.name


class OrderModel(Model):
    user_id = ForeignKey(UserModel, on_delete=CASCADE)
    item_id = ForeignKey(ItemModel, on_delete=CASCADE)
    quantity = IntegerField()

    def __str__(self) -> str:
        return self
