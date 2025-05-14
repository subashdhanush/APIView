from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
from  .serializers import ItemSerializer,EmployeeSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from myapi.models import Item,Employee

# Create your views here.
def index(request):
    students=[
        {'id':1,'name':'Subash','age':28}
    ]
    return HttpResponse(students)

@api_view(['GET','POST'])
def myapiview(request):
    if request.method == 'GET':
        items=Item.objects.all()
        serializer=ItemSerializer(items,many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)
    elif request.method == 'POST':
        serializer=ItemSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET','PUT','DELETE'])
def myapieditview(request,pk):
    try:
      items=Item.objects.get(pk=pk)
    except Item.DoesNotExist:
        return Response(status=status.HTTP_400_NOT_FOUND)
    if request.method == 'GET':
        serializer=ItemSerializer(items)
        return Response(serializer.data,status=status.HTTP_200_OK)
    elif request.method == 'PUT':
        serializer=ItemSerializer(items,data=request.data)          
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST) 
    elif request.method == 'DELETE':
        items.delete()
        return Response(status=status.HTTP_200_NO_CONTENT)

class Employees(APIView):
    def get(self,request):
        employees=Employee.objects.all()
        serializer=EmployeeSerializer(employees,many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)
    def post(self,request):
        serializer=EmployeeSerializer(data=request.data)
        if serializer.is_valid():
           serializer.save()
           return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)     

class EmployeeDetail(APIView):
    def get_object(self,pk):
        try:
            return Employee.objects.get(pk=pk)
        except Employees.DoesNotExist:
            raise Http404
    def get(self,request,pk):
        employee=self.get_object(pk)
        serializer=EmployeeSerializer(employee)
        return Response(serializer.data,status=status.HTTP_200_OK)
    def put(self,request,pk):
        employee=self.get_object(pk)
        serializer=EmployeeSerializer(employee,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_200_OK)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)                
    def delete(self,request,pk):
        employee=self.get_object(pk)
        employee.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)