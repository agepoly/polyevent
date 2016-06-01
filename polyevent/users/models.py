from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.utils import timezone

class PolyEventUserManager(BaseUserManager):
    def _create_user(self, username, password, is_superuser, is_staff, **extra_fields):
        now = timezone.now()
        if not username:
            raise ValueError('The given username must be set')
        user = self.model(username=username, is_active=True, is_superuser=is_superuser, last_login=now, date_joined=now, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    # Création des différents types de user et leur permissions
    def create_user(self, username, password=None, **extra_fields):
        return self._create_user(username, password, False, False, **extra_fields)
        user.save(using=self._db)
        return user

    def create_activityManager(self, username, password, **extra_fields):
        user = self._create_user(username, password, False, True, **extra_fields)
        user.save(using=self._db)
        return user

    def create_eventManager(self, username, password, **extra_fields):
        user = self._create_user(username, password, False, True, **extra_fields)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, password, **extra_fields):
        user = self._create_user(username, password, True, True, **extra_fields)
        user.save(using=self._db)
        return user

class PolyEventUser(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(max_length=255, unique=True)
    first_name = models.CharField(max_length=100, blank=False)
    last_name = models.CharField(max_length=100, blank=False)
    email = models.EmailField(max_length=255, blank=False)
    phone_number = models.CharField(max_length=30, blank=True, null=True)
    date_of_birth = models.DateField(blank=True, null=True)
    date_joined = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True, help_text=u"Défini si cet utilisateur doit être considéré comme actif. Désactiver ceci au lieu de supprimer le compte.")
    is_staff = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)

    GENDER_CHOICES = (
        ("H", u"Homme"),
        ("F", u"Femme"),
    )
    gender = models.CharField(max_length=5, default='H', choices=GENDER_CHOICES, blank=False, null=False)
    objects = PolyEventUserManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = []

    def get_full_name(self):
        return (self.first_name + " " + self.last_name) # removed unicode function

    def get_short_name(self):
        try:
            short_first = self.first_name.split(' ')[0]
            short_last = self.last_name[0]
            return (short_first + " " + short_last + ".") # Return "Johnny B." # removed unicode function
        except IndexError:
            return u"No name"

    def __unicode__(self):
        return ("{} [{}]").format(self.get_short_name(), self.get_number()) # removed unicode function
