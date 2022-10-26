
from .models import Status
from .serializers import StatusSerializer

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.generics import ListAPIView, CreateAPIView , RetrieveAPIView
# Create your views here.
class StatusApiView(APIView):
    def get(self, request, format=None):
        status_list = Status.objects.all()
        status_serializer = StatusSerializer(status_list, many=True)
        return Response(status_serializer.data)

# Create a list View 
class StatusListApiView(ListAPIView):
    queryset = Status.objects.all()
    serializer_class = StatusSerializer  


# CreateApiView  for Post any Content 
class StatusCreateApiView(CreateAPIView):
    queryset = Status.objects.all()
    serializer_class = StatusSerializer

#Watch a single post view by pk, id 
class StatusDetailsApiView(RetrieveAPIView):
    queryset= Status.objects.all()
    serializer_class = StatusSerializer
    lookup_field = "id"