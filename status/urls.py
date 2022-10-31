from django.urls import URLPattern, path
from .views import (StatusDetailsUpdateDeleteView,StatusListCreateView, StatusViewsets)

from rest_framework.routers import DefaultRouter

# status/ - List, Create => GET , POST
# status/<id>/ - Details,Delete, Update(Put/Patch)

# User viewset and Router create an API 
router = DefaultRouter()
router.register(r"viewsetapi", StatusViewsets, basename="views")

urlpatterns = [
    path('status/', StatusListCreateView.as_view()),
    path('status/<id>/', StatusDetailsUpdateDeleteView.as_view()),
 
] + router.urls