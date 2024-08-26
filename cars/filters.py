from dj_rql.filter_cls import AutoRQLFilterClass
from cars.models import Brand, Car


class BrandFilterClass(AutoRQLFilterClass):
    MODEL = Brand


class CarFilterClass(AutoRQLFilterClass):
    MODEL = Car
    FILTERS = [
        {
            'filter': 'brand',
            'source': 'brand__name',
        },
        {
            'filter': 'owner',
            'source': 'owner__username',
        },
    ]
