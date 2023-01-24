from usermanagement.models import User


class UserUtils:

    @staticmethod
    def get_user_by_id(user_id):
        try:
            return User.objects.get(id=user_id)
        except Exception:
            raise Exception('User doesnot exist')

    @staticmethod
    def get_user_by_phone_no(phone_no):
        try:
            return User.objects.get(phone_no=phone_no)
        except Exception:
            raise Exception('User doesnot exist')

    @staticmethod
    def check_user_exist(user_id):
        try:
            User.objects.get(id=user_id)
            return True
        except Exception:
            return False

    @staticmethod
    def check_existing_user(phone_no=None, email=None):
        try:
            if phone_no:
                return User.objects.get(phone_no=phone_no)
            elif email:
                return User.objects.get(email=email)
        except Exception:
            raise Exception('User doesnot exist')
