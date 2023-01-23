from django.contrib.auth.base_user import AbstractBaseUser
from django.db import models
from datetime import datetime
from usermanagement.account_user_manager import AccountUserManager


# Create your models here.


class User(AbstractBaseUser):
    first_name = models.CharField(db_column='FirstName', blank=False, null=False, max_length=16)
    last_name = models.CharField(db_column='LastName', blank=True, null=True, max_length=16)
    phone_no = models.CharField(db_column='PhoneNo', unique=True, blank=False, null=False, max_length=10)
    email = models.EmailField(db_column='Email', unique=True, blank=True, null=True, max_length=16)
    gender = models.CharField(db_column='Gender', null=True, blank=True, max_length=1)
    is_email_logged = models.BooleanField(db_column='IsEmailLogged', default=False)
    createdAt = models.DateTimeField(db_column='createdAt', default=datetime.now)
    modifiedAt = models.DateTimeField(db_column='modifiedAt', default=datetime.now)
    isDeleted = models.BooleanField(db_column='isDeleted', default=False)
    isActive = models.BooleanField(db_column='isActive', default=True)
    is_prime_user = models.BooleanField(db_column='isPrime', default=False)

    USERNAME_FIELD = 'phone_no'

    # REQUIRED_FIELDS = ['']

    objects = AccountUserManager()

    class Meta:
        db_table = 'Users'
