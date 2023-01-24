from django.forms import model_to_dict
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView

from usermanagement.account_user_manager import AccountUserManager
from usermanagement.user_otp_handler import UserOTPHandler


class CommitmentOtp(APIView):
    def post(self, request):
        try:
            payload_data = request.data
            code = UserOTPHandler.commitment(payload_data)
            return Response({'status': True, 'code': code}, 200)
        except Exception as e:
            return Response(str(e), 500)


class ValidateOtp(APIView):

    def post(self, request):
        try:
            payload_data = request.data
            success_status = UserOTPHandler.validate(payload_data)
            return Response({'status': success_status}, 200)
        except Exception as e:
            return Response(str(e), 500)


class SignUpAPIView(APIView):

    def post(self, request):
        try:
            payload = request.data
            user = AccountUserManager.create_user(payload)
            return Response({'success': True, 'user': user}, 200)
        except Exception as e:
            return Response(str(e), 500)


class MyTokenObtainPairSerializer(TokenObtainPairSerializer):

    def validate(self, attrs):
        data = super().validate(attrs)
        refresh = self.get_token(self.user)
        data["refresh"] = str(refresh)
        data["access"] = str(refresh.access_token)
        data["user"] = model_to_dict(self.user, exclude=['password'])
        return data


class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer
