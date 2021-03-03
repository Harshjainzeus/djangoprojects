from rest_framework import serializers
from .models import Department, Product


class DepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Department
        fields = ['id', 'department_name']


class ProductSerializer(serializers.ModelSerializer):
    department = DepartmentSerializer(read_only=True)

    class Meta:
        model = Product
        fields = ['id', 'title', 'department', 'seller', 'is_featured', 'cost', 'image_url']
