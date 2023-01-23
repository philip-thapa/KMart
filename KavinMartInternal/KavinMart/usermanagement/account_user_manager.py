from django.contrib.auth.base_user import BaseUserManager
from django.db.models import Q
from django.forms import model_to_dict

from usermanagement.models import User
from utils.validations import Validations


class AccountUserManager(BaseUserManager):

    @staticmethod
    def create_user(payload_data):
        AccountUserManager.validate_payload_data(payload_data)
        user = User(
            first_name=payload_data.get('firstName').strip(),
            last_name=payload_data.get('lastName').strip(),
            phone_no=payload_data.get('phoneNo').strip(),
        )
        user.set_password(payload_data.get('password').strip())
        user.save()
        return model_to_dict(user, exclude=['password'])

    @staticmethod
    def validate_payload_data(payload_data):
        if not payload_data.get('firstName').strip():
            raise Exception('First name is required')
        if not payload_data.get('password').strip():
            raise Exception('Password is required')

    @staticmethod
    def check_existing_user(email=None, phone=None):
        try:
            User.objects.get(Q(email=email) | Q(phone_no=phone))
            return True
        except Exception as e:
            return False
