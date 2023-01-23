from django.urls import path
from storeuser.api_views import StoreUserSignUpAPIView, UpdateStoreUserAPIView, DeleteStoreUserAPIView, \
    HardDeleteStoreUserAPIView, MyTokenObtainPairView, ChangeStoreUserRole
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    path(r'sign-up', StoreUserSignUpAPIView.as_view(), name='store-user-sign-up'),
    path(r'sign-in', MyTokenObtainPairView.as_view(), name='sign-in'),
    path(r'update-user', UpdateStoreUserAPIView.as_view(), name='update-user'),
    path(r'delete-user', DeleteStoreUserAPIView.as_view(), name='delete-user'),
    path(r'hard-delete-user', HardDeleteStoreUserAPIView.as_view(), name='hard-delete-user'),
    path('api/token/refresh', TokenRefreshView.as_view(), name='token_refresh'),
    path(r'change-user-role', ChangeStoreUserRole.as_view(), name='change-user-role')
]