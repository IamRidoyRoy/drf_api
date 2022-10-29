
from .models import Status
from .serializers import StatusSerializer

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.generics import ListAPIView, CreateAPIView , RetrieveAPIView, UpdateAPIView, DestroyAPIView
from rest_framework import mixins
# Create your views here.


# Create Api and watch Api view list 
class StatusListCreateView(mixins.CreateModelMixin,ListAPIView):
    queryset = Status.objects.all()
    serializer_class = StatusSerializer

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)



#Watch a single post view, update or delete
class StatusDetailsApiView(mixins.UpdateModelMixin, mixins.DestroyModelMixin,RetrieveAPIView):
    queryset= Status.objects.all()
    serializer_class = StatusSerializer
    lookup_field = "id"

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)
    
    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)
    
    