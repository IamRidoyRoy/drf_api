from django.urls import URLPattern, path
from .views import (StatusDetailsUpdateDeleteView,StatusListCreateView)

# status/ - List, Create => GET , POST
# status/<id>/ - Details,Delete, Update(Put/Patch)
urlpatterns = [
    path('status/', StatusListCreateView.as_view()),
    path('status/<id>/', StatusDetailsUpdateDeleteView.as_view())
 
] 