from django.urls import path
from usermanagement.api_views import CommitmentOtp, UserSignUpAPIView, ValidateOtp

urlpatterns = [
    path(r'generate-otp', CommitmentOtp.as_view(), name='generate-otp'),
    path(r'verify-otp', ValidateOtp.as_view(), name='verify-otp'),
    path(r'sign-up', UserSignUpAPIView.as_view(), name='store-user-sign-up')
]
