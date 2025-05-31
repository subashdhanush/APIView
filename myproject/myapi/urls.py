from django.urls import path,include
from .import views
from rest_framework.routers import DefaultRouter


router=DefaultRouter()
router.register('employee',views.EmployeeViewset,basename='employee')



urlpatterns = [
    # path('index',views.index,name='index'),
    # path('myapiview/',views.myapiview),
    # path('myapiview/<int:pk>/',views.myapieditview),
    # path('employee/',views.Employees.as_view()),
    # path('employees/<int:pk>/',views.EmployeeDetail.as_view()),
    path('',include(router.urls)),
    path('blogs/',views.BlogView.as_view()),
    path('comments/',views.CommentsView.as_view())
]