from django.urls import URLPattern, path
from .views import StatusApiView
urlpatterns = [
    path('api/', StatusApiView.as_view())
]