from django.urls import path, include
from rest_framework.routers import DefaultRouter

from api import views

router = DefaultRouter()
router.register(r'employees', views.EmployeeViewSet)



urlpatterns = [
    path('', include(router.urls)),
    path('reports/employees/age/', views.EmployeeViewAge.as_view()),
    path('reports/employees/salary/', views.EmployeeViewSalary.as_view()),
]