from django.urls import path
from storeuser.api_views import StoreUserSignUpAPIView, UpdateStoreUserAPIView, DeleteStoreUserAPIView, \
    HardDeleteStoreUserAPIView

urlpatterns = [
    path(r'sign-up', StoreUserSignUpAPIView.as_view(), name='store-user-sign-up'),
    path(r'update-user', UpdateStoreUserAPIView.as_view(), name='update-user'),
    path(r'delete-user', DeleteStoreUserAPIView.as_view(), name='delete-user'),
    path(r'hard-delete-user', HardDeleteStoreUserAPIView.as_view(), name='hard-delete-user')
]