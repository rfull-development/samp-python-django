# Copyright (c) 2023 RFull Development
# This source code is managed under the MIT license. See LICENSE in the project root.
from api.models import UserModel
from django.test import TestCase


class UserModelTests(TestCase):
    def test_user_add(self):
        """
        test_user_add() tests the addition of a user to the database.
        """
        user = UserModel()
        user.name = 'Test User'
        user.password = 'test'
        user.save()

        self.assertEqual(user.name, 'Test User')
        self.assertEqual(user.password, 'test')
        self.assertEqual(user.id, 1)
