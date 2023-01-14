from django.forms import model_to_dict
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from storeuser.store_user_account_manager import StoreUsermanager


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
