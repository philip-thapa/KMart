from usermanagement.module_group_mapping import ModuleGroupsMapping
from usermanagement.module_groups import ModuleGroups


class Users:

    @staticmethod
    def is_app_admin(request):
        return any(map(lambda each: each in ModuleGroupsMapping[ModuleGroups.ADMIN], request.user.roles))

    @staticmethod
    def is_staff(request):
        return bool(request.user and request.user.is_authenticated)

    @staticmethod
    def is_manager(request):
        return any(map(lambda each: each in ModuleGroupsMapping[ModuleGroups.MANAGER], request.user.roles))

    @staticmethod
    def is_store_employee(request):
        return any(map(lambda each: each in ModuleGroupsMapping[ModuleGroups.STORE_EMPLOYEE], request.user.roles))

    @staticmethod
    def is_delivery_guy(request):
        return any(map(lambda each: each in ModuleGroupsMapping[ModuleGroups.DELIVERY_GUY], request.user.roles))
