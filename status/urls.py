from django.urls import URLPattern, path
from .views import (StatusDetailsApiView,StatusListCreateView)

# status/ - List, Create => GET , POST
# status/<id>/ - Details,Delete, Update(Put/Patch)
urlpatterns = [
    path('status/', StatusListCreateView.as_view()),
    path('status/<id>/', StatusDetailsApiView.as_view())
 
] 