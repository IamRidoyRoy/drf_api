from django.urls import URLPattern, path
from .views import StatusApiView, StatusCreateApiView, StatusListApiView
urlpatterns = [
    path('status/', StatusApiView.as_view()),
    path('status/list/', StatusListApiView.as_view()),
    path('status/create/', StatusCreateApiView.as_view())
]