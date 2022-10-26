from django.urls import URLPattern, path
from .views import StatusApiView, StatusListApiView
urlpatterns = [
    path('status/', StatusApiView.as_view()),
    path('status/list/', StatusListApiView.as_view())
]