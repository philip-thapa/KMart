from django.forms import model_to_dict
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

from storeuser.end_user_manager import EndUserManager
from storeuser.store_user_account_manager import StoreUsermanager
from storeuser.store_user_manager import StoreUserManager


# Create your views here.


class StoreUserSignUpAPIView(APIView):

    def post(self, request):
        try:
            payload = request.data
            user = StoreUsermanager.create_store_user(payload)
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


class UpdateStoreUserAPIView(APIView):

    def post(self, request):
        try:
            payload = request.data
            user = StoreUsermanager.update_store_user(payload)
            return Response({'success': True, 'user': user}, 200)
        except Exception as e:
            return Response(str(e), 500)


class DeleteStoreUserAPIView(APIView):

    def get(self, request):
        try:
            id = request.query_params
            StoreUsermanager.deleteStoreUser(id)
            return Response({'success': True}, 200)
        except Exception as e:
            return Response(str(e), 500)


class HardDeleteStoreUserAPIView(APIView):

    def get(self, request):
        try:
            id = request.query_params
            StoreUsermanager.hardDelete(id)
            return Response({'success': True}, 200)
        except Exception as e:
            return Response(str(e), 500)


class GetStoreUserDetailsAPIView(APIView):

    def get(self, request):
        try:
            id = request.query_params
            user = StoreUsermanager.getStoreUserDetails(id)
            return Response({'success': True, 'user': user}, 200)
        except Exception as e:
            return Response(str(e), 500)


class GetAllStoreUsersAPIView(APIView):

    def get(self, request):
        try:
            users = StoreUsermanager.getAllUsers()
            return Response({'success': True, 'users': users}, 200)
        except Exception as e:
            return Response(str(e), 500)


class ChangeStoreUserRole(APIView):

    def get(self, request):
        try:
            filters = request.query_params
            user_id = filters.get('userId')
            user = StoreUserManager(user_id).change_user_role(filters)
            return Response({'success': True, 'user': user}, 200)
        except Exception as e:
            return Response(str(e), 500)


class GetUser(APIView):

    def get(self, request):
        try:
            filters = request.query_params
            user_id = filters.get('userId')
            user = EndUserManager().get_user(user_id)
            return Response({'success': True, 'user': user}, 200)
        except Exception as e:
            return Response(str(e), 500)


class GetAllUserList(APIView):

    def get(self, request):
        try:
            users = EndUserManager().get_all_end_user_list()
            return Response({'success': True, 'users': users}, 200)
        except Exception as e:
            return Response(str(e), 500)


class DeactivateUser(APIView):

    def get(self, request):
        try:
            filters = request.query_params
            user_id = filters.get('userId')
            EndUserManager().deactive_user(user_id)
            return Response({'success': True}, 200)
        except Exception as e:
            return Response(str(e), 500)
