from django.test import TestCase

from authentication.factories import UserFactory


class TestFactories(TestCase):
    def test_user_factory(self):
        user = UserFactory()
        self.assertIsNotNone(user.email)
        self.assertIsNotNone(user.fullname)
        self.assertTrue(user.is_active)
        