from django.urls import path
from usermanagement.api_views import CommitmentOtp, SignUpAPIView, ValidateOtp, MyTokenObtainPairView
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    path(r'generate-otp', CommitmentOtp.as_view(), name='generate-otp'),
    path(r'verify-otp', ValidateOtp.as_view(), name='verify-otp'),
    path(r'sign-up', SignUpAPIView.as_view(), name='store-user-sign-up'),
    path(r'sign-in', MyTokenObtainPairView.as_view(), name='sign-in'),
    path('api/token/refresh', TokenRefreshView.as_view(), name='token_refresh'),
]