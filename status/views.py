
from .models import Status
from .serializers import StatusSerializer
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework import parsers
# Create your views here.


# Create Api and watch Api view list 
class StatusListCreateView(ListCreateAPIView):
    queryset = Status.objects.all()
    serializer_class = StatusSerializer
    parser_classes = [parsers.FormParser, parsers.MultiPartParser]

#Watch a single post view, update or delete
class StatusDetailsUpdateDeleteView(RetrieveUpdateDestroyAPIView):
    queryset= Status.objects.all()
    serializer_class = StatusSerializer
    lookup_field = "id"
    parser_classes = [parsers.FormParser, parsers.MultiPartParser]

    
    