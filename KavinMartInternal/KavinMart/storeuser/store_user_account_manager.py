from django.contrib.auth.models import BaseUserManager
from django.forms import model_to_dict

import storeuser.models
from storeuser.constants import GENDER, UerDetails
from utils.validations import Validations


class StoreUsermanager(BaseUserManager):

    @staticmethod
    def create_store_user(payload_data):
        StoreUsermanager.validate_payload_data(payload_data)
        user = storeuser.models.StoreUsers(
            payload_data.get('user_id'),
            payload_data.get('first_name'),
            payload_data.get('last_name'),
            payload_data.get('phone_no'),
            payload_data.get('email'),
            payload_data.get('address'),
            payload_data.get('aadhar_no'),
            payload_data.get('pan_no'),
            payload_data.get('role'),
            payload_data.get('dob'),
            payload_data.get('father_name'),
            payload_data.get('gender')
        )
        user.set_password(payload_data.get('password'))
        user.save()
        return model_to_dict(user, exclude=['password'])

    def create_superuser(self, payload_data):
        return self.create_user(payload_data)

    @staticmethod
    def update_store_user(payload):
        user_id = payload.get('id')
        try:
            user = storeuser.models.StoreUsers.objects.get(id=user_id)
        except Exception as e:
            raise Exception('Store User doesnot exist')
        if payload.get('firstName'):
            user.first_name = payload.get('firstName')
        if payload.get('lastName'):
            user.last_name = payload.get('lastName')
        if payload.get('email'):
            user.email = payload.get('email')
        if payload.get('address'):
            user.address = payload.get('address')
        if payload.get('aadharNo'):
            user.aadhar_no = payload.get('aadharNo')
        if payload.get('panNo'):
            user.pan_no = payload.get('panNo')
        if payload.get('fatherName'):
            user.father_name = payload.get('fatherName')
        user.save()
        return user


    @staticmethod
    def validate_payload_data(payload_data):
        if not payload_data.user_id:
            raise ValueError('User must have User ID')
        if not payload_data.first_name:
            raise ValueError('User must have First Name')
        if not payload_data.phone_no:
            raise ValueError('User must have Phone Number')
        if not Validations.phone_no_validation(payload_data.phone_no):
            raise Exception('Phone number is not valid')
        if not payload_data.address:
            raise ValueError('User must have Address')
        if not payload_data.role:
            raise ValueError('User must have Role')
        if not payload_data.dob:
            raise ValueError('User must have DOB')
        if not payload_data.father_name:
            raise ValueError('User must have father name')
        if not payload_data.gender:
            raise ValueError('User must have Gender')
        if payload_data.gender not in GENDER:
            raise Exception('Invalid Gender')
        if not payload_data.password:
            raise Exception('Password is required')

    @staticmethod
    def deleteStoreUser(id):
        try:
            user = storeuser.models.StoreUsers.objects.get(id=id)
        except Exception as e:
            raise Exception('User ID doesnot exist')
        user.isActive = False
        user.isDeleted = True
        user.save()

    @staticmethod
    def hardDelete(id):
        try:
            user = storeuser.models.StoreUsers.objects.get(id=id)
        except Exception as e:
            raise Exception('User ID doesnot exist')
        user.delete()

    @staticmethod
    def getStoreUserDetails(id):
        try:
            user = storeuser.models.StoreUsers.objects.get(id=id)
        except Exception as e:
            raise Exception("User ID doesnot exist")

    @staticmethod
    def getAllUsers():
        return list(storeuser.models.StoreUsers.objects.values(*UerDetails.values))
