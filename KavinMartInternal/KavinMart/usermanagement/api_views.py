from django.forms import model_to_dict
from rest_framework.views import APIView
from rest_framework.response import Response
from usermanagement.account_user_manager import AccountUserManager
from utils.otp_handler import OTP
from utils.validations import Validations


class CommitmentOtp(APIView):
    def post(self, request):
        try:
            data = request.data
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
            return Response({'status': True, 'code': code}, 200)
        except Exception as e:
            return Response(str(e), 500)


class ValidateOtp(APIView):

    def post(self, request):
        try:
            success_status = False
            data = request.data
            email = data.get('email')
            phone = data.get('phone')
            code = data.get('otp')
            otp = None
            userdata = None
            if phone:
                otp = OTP(dict(phone=phone), digits=4)
            elif email:
                otp = OTP(dict(email=email), digits=4)
            is_verified = otp.verify(code)
            if is_verified:
                success_status = True
            return Response({'status': success_status, 'user': userdata}, 200)

        except Exception as e:
            return Response(str(e), 500)


class UserSignUpAPIView(APIView):

    def post(self, request):
        try:
            payload = request.data
            user = AccountUserManager.create_user(payload)
            return Response({'success': True, 'user': user}, 200)
        except Exception as e:
            return Response(str(e), 500)