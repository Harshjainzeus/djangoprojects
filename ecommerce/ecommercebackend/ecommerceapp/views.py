from django.shortcuts import render
from django.views import View
from django.http import HttpResponse
from rest_framework import viewsets, permissions
from .models import Product, Department
from .serializer import DepartmentSerializer, ProductSerializer

# Create your views here.


def index(request):
    return HttpResponse("hello ")


class DepartmentViewset(viewsets.ModelViewSet):
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer


class ProductViewset(viewsets.ModelViewSet):
    permission_classes = [permissions.AllowAny]
    authentication_classes = []


    def get_queryset(self):

        queryset = Product.objects.all()
        featured = self.request.query_params.get('is_featured', None)
        department = self.request.query_params.get('department', None)
        department_id = Department.objects.filter(department_name=department)

        if featured is not None:
            queryset = queryset.filter(is_featured=True)
        elif department is not None:
            queryset = queryset.filter(department=department_id[0].id)
        return queryset
    serializer_class = ProductSerializer

