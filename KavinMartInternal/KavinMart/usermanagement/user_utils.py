from usermanagement.models import Users


class UserUtils:

    @staticmethod
    def get_user_by_id(user_id):
        try:
            return Users.objects.get(id=user_id)
        except Exception:
            raise Exception('User doesnot exist')

    @staticmethod
    def get_user_by_phone_no(phone_no):
        try:
            return Users.objects.get(phone_no=phone_no)
        except Exception:
            raise Exception('User doesnot exist')

    @staticmethod
    def check_user_exist(user_id):
        try:
            Users.objects.get(id=user_id)
            return True
        except Exception:
            return False

    @staticmethod
    def check_existing_user(phone_no=None, email=None):
        try:
            if phone_no:
                return Users.objects.get(phone_no=phone_no)
            elif email:
                return Users.objects.get(email=email)
        except Exception:
            raise Exception('User doesnot exist')
