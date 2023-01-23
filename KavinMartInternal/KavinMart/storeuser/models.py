from django.db import models
import jsonfield
from datetime import datetime
from django.contrib.auth.models import AbstractBaseUser
from rest_framework.fields import JSONField
from utils.custom_models import CustomModel

from storeuser.store_user_account_manager import StoreUsermanager


class StoreUsers(AbstractBaseUser):
    user_id = models.CharField(db_column='StoreUserID', unique=True, blank=False, null=False, max_length=24)
    first_name = models.CharField(db_column='FirstName', blank=False, null=False, max_length=16)
    last_name = models.CharField(db_column='LastName', blank=True, null=True, max_length=16)
    phone_no = models.CharField(db_column='PhoneNo', unique=True, blank=False, null=False, max_length=10)
    email = models.EmailField(db_column='Email', blank=True, null=True, max_length=16)
    address = models.CharField(db_column='Address', blank=True, null=True, max_length=256)
    aadhar_no = models.CharField(db_column='AadharNo', blank=True, null=True, max_length=12)
    pan_no = models.CharField(db_column='PanNo', blank=True, null=True, max_length=10)
    # role = jsonfield.JSONField(db_column='ROLE', blank=False, null=False, max_length=256)
    role = JSONField(default=['staff'])
    dob = models.DateField(db_column='DOB', null=True, blank=True)
    father_name = models.CharField(db_column='FatherName', null=True, blank=True, max_length=24)
    gender = models.CharField(db_column='Gender', null=True, blank=True, max_length=1)
    createdAt = models.DateTimeField(db_column='createdAt', default=datetime.now)
    modifiedAt = models.DateTimeField(db_column='modifiedAt', default=datetime.now)
    isDeleted = models.BooleanField(db_column='isDeleted', default=False)
    isActive = models.BooleanField(db_column='isActive', default=True)

    USERNAME_FIELD = 'user_id'

    # REQUIRED_FIELDS = ['']

    objects = StoreUsermanager()

    class Meta:
        db_table = 'StoreUsers'


class Roles(CustomModel):
    role = models.CharField(db_column='role', max_length=16, unique=True, blank=False, null=False)
    created_by = models.CharField(db_column='created_by', max_length=16, blank=True, null=True)
