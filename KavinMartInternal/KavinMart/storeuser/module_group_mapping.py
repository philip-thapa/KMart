from storeuser.module_groups import ModuleGroups
from storeuser.roles import Roles

ModuleGroupsMapping = {
    ModuleGroups.ADMIN: [
        Roles.ROLE_ADMIN
    ],

    ModuleGroups.MANAGER: [
        Roles.ROLE_MANAGER
    ],

    ModuleGroups.STORE_EMPLOYEE: [
        Roles.ROLE_STORE_EMPLOYEE
    ],

    ModuleGroups.DELIVERY_GUY: [
        Roles.ROLE_DELIVERY_GUY
    ]
}