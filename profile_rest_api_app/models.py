from django.contrib.auth.models import (
    BaseUserManager, AbstractBaseUser
)
from django.db import models
from profile_rest_api_project import settings


class MyUserManager(BaseUserManager):
    def create_user(self, email, username, DOB, password=None):
        '''it must contain all required fields
            creating a user '''
        user_obj = self.model(
            email=self.normalize_email(email),
            username=username,
            DOB=DOB,
        )
        user_obj.set_password(password)
        user_obj.save(using=self._db)
        return user_obj

    def create_superuser(self, email, username, DOB, password=None):
        '''It must contain all required fields
            creating a superuser'''
        user_obj = self.create_user(
            email,
            username=username,
            DOB=DOB,
            password=password
        )
        user_obj.is_superuser = True
        user_obj.is_staff = True
        user_obj.save(using=self._db)
        return user_obj


class MyUser(AbstractBaseUser):
    """ model class to define custom User Authentication"""
    email = models.EmailField(max_length=255, unique=True)
    username = models.CharField(max_length=30, unique=True)
    DOB = models.DateField()
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    # no need to include USERNAME_FIELD and password as they are mandatory fields"
    REQUIRED_FIELDS = ['username', 'DOB', ]

    objects = MyUserManager()                 # call the model manager.

    def get_full_name(self):
        # The user is identified by their email address
        return self.email

    def get_short_name(self):
        # The user is identified by their email address
        return self.email

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return True

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True


class UserStatusFeed(models.Model):
    ''' Setting up a model to save User Status'''
    user_profile_id = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE
    )
    status_feed = models.CharField(max_length=255)
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.status_feed
