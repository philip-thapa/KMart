from django.contrib.auth.base_user import BaseUserManager
from django.forms import model_to_dict

from usermanagement.models import User
from utils.validations import Validations


class AccountUserManager(BaseUserManager):

    @staticmethod
    def create_store_user(payload_data):
        AccountUserManager.validate_payload_data(payload_data)
        is_email = False
        if payload_data.get('email'):
            is_email = True
        user = User(
            phone_no=payload_data.get('phoneNo'),
            email=payload_data.get('email').strip(),
            is_email_logged=is_email,
        )
        user.set_password(payload_data.get('password').strip())
        user.save()
        return model_to_dict(user, exclude=['password'])

    @staticmethod
    def validate_payload_data(payload_data):
        if not payload_data.get('phoneNo').strip() or not payload_data.get('email').strip():
            raise Exception('Phone or Email is required')
        if payload_data.get('phoneNo').strip() and not Validations.phone_no_validation(payload_data.get('phoneNo')):
            raise Exception('Invalid phone number')
        if payload_data.get('email').strip() and not Validations.email_validation(payload_data.get('email')):
            raise Exception('Invalid email address')
