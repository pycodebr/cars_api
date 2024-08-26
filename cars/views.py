from dj_rql.drf import RQLFilterBackend
from rest_framework import viewsets, permissions
from cars.filters import BrandFilterClass, CarFilterClass
from cars.models import Brand, Car
from cars.permissions import CarOwnerPermission
from cars.serializers import BrandModelSerializer, CarModelSerializer


class BrandModelViewSet(viewsets.ModelViewSet):
    queryset = Brand.objects.all()
    serializer_class = BrandModelSerializer
    filter_backends = [RQLFilterBackend]
    rql_filter_class = BrandFilterClass


class CarModelViewSet(viewsets.ModelViewSet):
    queryset = Car.objects.all()
    serializer_class = CarModelSerializer
    filter_backends = [RQLFilterBackend]
    rql_filter_class = CarFilterClass
    permission_classes = [permissions.DjangoModelPermissions, CarOwnerPermission,]
