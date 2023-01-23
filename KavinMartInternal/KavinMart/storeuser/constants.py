class GENDER:
    MALE = 'M'
    FEMALE = 'F'
    BOTH = [MALE, FEMALE]


class UerDetails:
    values = ('user_id', 'first_name', 'last_name', 'phone_no', 'email',
              'address', 'aadhar_no', 'pan_no', 'role', 'dob', 'father_name', 'gender')


class UserRoles:
    Admin = 'Admin'
    Manager = 'Manager'
    DeliveryGuy = 'DeliveryGuy'
    StorePerson = 'StorePerson'
    All = [Admin, Manager, DeliveryGuy, StorePerson]
