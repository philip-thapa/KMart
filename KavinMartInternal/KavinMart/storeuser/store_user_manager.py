from django.forms import model_to_dict

from storeuser.models import StoreUsers
from storeuser.constants import UserRoles


class StoreUserManager:

    def __init__(self, userid=None):
        self.store_user = None
        if userid:
            self.store_user = StoreUsers.objects.get(id=userid)

    def change_user_role(self, data):
        roles = data.get('roles')
        invalid_roles = set()
        for role in roles:
            if role not in UserRoles.All:
                invalid_roles.add(role)
        if invalid_roles:
            raise Exception("Roles doesnot exist " + ", ".join(role for role in invalid_roles))
        self.store_user.role = {'roles': set(roles)}
        self.save()
        return self.store_user


