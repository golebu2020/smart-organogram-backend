from django.urls import path
from . import views

urlpatterns = [
    # http://127.0.0.1:8000/api/organogram/
    path('organogram/', views.OrganogramList.as_view(), name="organogram-list"),
    path('update-vacant/', views.UpdateVacantEmployee.as_view(), name="update-vacant"),
]
