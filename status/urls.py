from django.urls import URLPattern, path
from .views import StatusApiView, StatusCreateApiView, StatusDetailsApiView, StatusListApiView, UpdateApiContent,DeleteStatus
urlpatterns = [
    path('status/', StatusApiView.as_view()),
    path('status/list/', StatusListApiView.as_view()),
    path('status/create/', StatusCreateApiView.as_view()),
    path('status/details/<id>/', StatusDetailsApiView.as_view()),
    path('status/update/<id>/', UpdateApiContent.as_view()),
    path('status/delete/<id>/',DeleteStatus.as_view()),
]