import base64
from pyotp.totp import TOTP
from KavinMart.settings import OTP_SECRET_KEY


class OTP:
    def __init__(self, data, digits):
        self.data = data
        self.secret_key = OTP_SECRET_KEY
        self.digits = digits
        self._generate_key()
        self._initiate_t_otp()

    def _generate_key(self):
        data = self.data
        if not isinstance(data, str):
            data = str(self.data)
        self.key = base64.b32encode((data + self.secret_key).encode())

    def _initiate_t_otp(self):
        self.t_otp = TOTP(self.key, digits=self.digits, interval=600)

    def generate_otp(self):
        return self.t_otp.now()

    def verify(self, code):
        return self.t_otp.verify(code)
