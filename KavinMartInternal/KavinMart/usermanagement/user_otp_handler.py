from utils.otp_handler import OTP
from utils.validations import Validations


class UserOTPHandler:

    @staticmethod
    def commitment(data):
        email = data.get('email')
        phone = data.get('phone')
        otp = None
        if email:
            Validations.email_validation(email)
            otp = OTP(dict(email=email), 4)
        elif phone:
            Validations.phone_no_validation(phone)
            otp = OTP(dict(phone=phone), 4)
        code = otp.generate_otp()
        print(code)
        return code

    @staticmethod
    def validate(data):
        success_status = False
        email = data.get('email')
        phone = data.get('phone')
        code = data.get('otp')
        otp = None
        if phone:
            otp = OTP(dict(phone=phone), digits=4)
        elif email:
            otp = OTP(dict(email=email), digits=4)
        is_verified = otp.verify(code)
        if is_verified:
            success_status = True
        return success_status
