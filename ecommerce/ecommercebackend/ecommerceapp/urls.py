from django.urls import path
from rest_framework import routers

from .views import DepartmentViewset, ProductViewset


router = routers.SimpleRouter()
router.register(r'department', DepartmentViewset, basename="departmentwise")
router.register(r'products', ProductViewset, basename="products")

urlpatterns = router.urls
