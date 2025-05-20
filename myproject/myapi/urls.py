from django.urls import path
from .import views


urlpatterns = [
    # path('index',views.index,name='index'),
    # path('myapiview/',views.myapiview),
    # path('myapiview/<int:pk>/',views.myapieditview),
    path('employee/',views.Employees.as_view()),
    path('employees/<int:pk>/',views.EmployeeDetail.as_view()),
]