from rest_framework import serializers
from myapi.models import Item,Employee


class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model= Item
        fields="__all__"

class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model= Employee
        fields="__all__"        