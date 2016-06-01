from django.test import TestCase
from django.contrib.auth import get_user_model
from datetime import date
from users.models import PolyEventUser, PolyEventUserManager

class UserTestCase(TestCase):
    def setup_users(self):
        get_user_model().objects.create_user(username="1", first_name="Jean", last_name="Dupont", email="jean@dupont.org", phone_number="0123456789", date_of_birth="2001-01-01")
        get_user_model().objects.create_user(username=2, password="root", gender="F")
        get_user_model().objects.create_activityManager(username=3, password="root")
        get_user_model().objects.create_eventManager(username=4, password="root")
        get_user_model().objects.create_superuser(username=5, password="root")

    def test_create_user_correctly_save_infos(self):
        self.setup_users()
        user1 = PolyEventUser.objects.get(pk=1)
        self.assertEqual(user1.username, "1")
        self.assertEqual(user1.first_name, "Jean")
        self.assertEqual(user1.last_name, "Dupont")
        self.assertEqual(user1.get_full_name(), "Jean Dupont")
        self.assertEqual(user1.get_short_name(), "Jean D.")
        self.assertEqual(user1.email, "jean@dupont.org")
        self.assertEqual(user1.phone_number, "0123456789")
        self.assertEqual(user1.date_of_birth, date(2001, 1, 1))
        self.assertEqual(user1.is_staff, False)
        self.assertEqual(user1.is_superuser, False)
