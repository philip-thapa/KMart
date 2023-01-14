import re


class Validations:

    @staticmethod
    def phone_no_validation(phone_no):
        pattern = re.compile("(0|91)?[6-9][0-9]{9}")
        return pattern.match(phone_no)