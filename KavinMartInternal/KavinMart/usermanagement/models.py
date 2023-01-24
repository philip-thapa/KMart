from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager
from django.db import models
from datetime import datetime
from django.forms import model_to_dict
from utils.custom_models import CustomModel


class AccountUserManager(BaseUserManager):

    @staticmethod
    def create_user(payload_data):
        AccountUserManager.validate_payload_data(payload_data)
        user = Users(
            first_name=payload_data.get('firstName').strip(),
            last_name=payload_data.get('lastName').strip(),
            phone_no=payload_data.get('phoneNo').strip(),
        )
        user.set_password(payload_data.get('password').strip())
        user.save()
        user_log = UserLog(
            user_id_id=user.id,
            first_name=payload_data.get('firstName').strip(),
            last_name=payload_data.get('lastName').strip(),
            phone_no=payload_data.get('phoneNo').strip(),
        )
        user_log.save()
        return model_to_dict(user, exclude=['password'])

    @staticmethod
    def validate_payload_data(payload_data):
        if not payload_data.get('firstName').strip():
            raise Exception('First name is required')
        if not payload_data.get('password').strip():
            raise Exception('Password is required')

# Create your models here.
gender_choice = (
    ('M', 'M'),
    ('F', 'F'),
    ('', '')
)


class Users(AbstractBaseUser):
    first_name = models.CharField(db_column='FirstName', blank=False, null=False, max_length=16)
    last_name = models.CharField(db_column='LastName', blank=True, null=True, max_length=16)
    phone_no = models.CharField(db_column='PhoneNo', unique=True, blank=False, null=False, max_length=10)
    email = models.EmailField(db_column='Email', unique=True, blank=True, null=True, max_length=16)
    is_email_verified = models.BooleanField(db_column='IsEmailVerified', default=False)
    is_prime_user = models.BooleanField(db_column='isPrime', default=False)
    is_store_user = models.BooleanField(db_column='isStoreUser', default=False)
    roles = models.JSONField(db_column='ROLES', default=[])
    createdAt = models.DateTimeField(db_column='createdAt', default=datetime.now)
    modifiedAt = models.DateTimeField(db_column='modifiedAt', default=datetime.now)
    isDeleted = models.BooleanField(db_column='isDeleted', default=False)
    isActive = models.BooleanField(db_column='isActive', default=True)

    USERNAME_FIELD = 'phone_no'

    # REQUIRED_FIELDS = ['']

    objects = AccountUserManager()

    class Meta:
        db_table = 'Users'


class StoreUserDetails(CustomModel):
    employee_id = models.ForeignKey(Users, related_name="store_employee_id", on_delete=models.CASCADE,
                                    db_column="EmployeeID")
    user_id = models.CharField(db_column='StoreUserID', unique=True, blank=False, null=False, max_length=24)
    address = models.CharField(db_column='Address', blank=True, null=True, max_length=256)
    aadhar_no = models.CharField(db_column='AadharNo', blank=True, null=True, max_length=12)
    pan_no = models.CharField(db_column='PanNo', blank=True, null=True, max_length=10)
    dob = models.DateField(db_column='DOB', null=True, blank=True)
    father_name = models.CharField(db_column='FatherName', null=True, blank=True, max_length=24)
    gender = models.CharField(db_column='Gender', max_length=1, choices=gender_choice, default='')
    alternate_phone_no = models.CharField(db_column='alternatePhone', null=True, blank=True, max_length=10)


class Address(CustomModel):
    primary_address = models.TextField(db_column='primaryAddress', blank=True, null=True)
    secondary_address = models.TextField(db_column='secondary_address', blank=True, null=True)


class UserLog(CustomModel):
    user_id = models.ForeignKey(Users, related_name="user_id_log", on_delete=models.CASCADE, db_column="userID")
    first_name = models.CharField(db_column='FirstName', blank=False, null=False, max_length=16)
    last_name = models.CharField(db_column='LastName', blank=True, null=True, max_length=16)
    phone_no = models.CharField(db_column='PhoneNo', unique=True, blank=False, null=False, max_length=10)
    email = models.EmailField(db_column='Email', unique=True, blank=True, null=True, max_length=16)
    is_email_verified = models.BooleanField(db_column='IsEmailVerified', default=False)
    is_prime_user = models.BooleanField(db_column='isPrime', default=False)
    is_store_user = models.BooleanField(db_column='isStoreUser', default=False)
    roles = models.JSONField(db_column='ROLES', default=[])


class Roles(CustomModel):
    role_name = models.CharField(db_column='roleName', unique=True)
