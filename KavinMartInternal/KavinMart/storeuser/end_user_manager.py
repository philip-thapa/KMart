from django.forms import model_to_dict

from usermanagement.models import User


class EndUserManager:

    @staticmethod
    def get_user(user_id):
        return model_to_dict(User.objects.get(id=user_id))

    @staticmethod
    def get_all_end_user_list():
        users = list(User.objects.values())
        return users

    @staticmethod
    def deactive_user(user_id):
        user = User.objects.get(id=user_id)
        user.isDeleted = True
        user.isActive = False
