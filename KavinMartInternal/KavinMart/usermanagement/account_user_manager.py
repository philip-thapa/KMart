from django.contrib.auth.base_user import BaseUserManager
from django.forms import model_to_dict
from usermanagement.models import User, UserLog


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
