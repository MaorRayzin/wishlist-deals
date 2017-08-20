from rest_framework.response import Response
from rest_framework.views import APIView

# Create your views here.


class Wishlist(APIView):

    def get(self, request):
        return Response('Hello World!')