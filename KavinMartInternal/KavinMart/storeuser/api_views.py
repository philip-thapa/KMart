from rest_framework.views import APIView
from rest_framework.response import Response
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
