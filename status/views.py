import imp
from django.shortcuts import render
from .models import Status
from .serializers import StatusSerializer

from rest_framework.views import APIView
from rest_framework.response import Response

# Create your views here.
class StatusApiView(APIView):
    def get(self, request, format=None):
        status_list = Status.objects.all()
        status_serializer = StatusSerializer(status_list, many=True)
        return Response(status_serializer.data)
