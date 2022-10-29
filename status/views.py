
from .models import Status
from .serializers import StatusSerializer

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
# from rest_framework import mixins
# Create your views here.


# Create Api and watch Api view list 
class StatusListCreateView(ListCreateAPIView):
    queryset = Status.objects.all()
    serializer_class = StatusSerializer

#Watch a single post view, update or delete
class StatusDetailsApiView(RetrieveUpdateDestroyAPIView):
    queryset= Status.objects.all()
    serializer_class = StatusSerializer
    lookup_field = "id"

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)
    
    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)
    
    