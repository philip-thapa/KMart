import re


class Validations:

    @staticmethod
    def phone_no_validation(phone_no):
        pattern = re.compile("(0|91)?[6-9][0-9]{9}")
        return pattern.match(phone_no)

    @staticmethod
    def email_validation(email):
        email_regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
        return re.fullmatch(email_regex, email)
