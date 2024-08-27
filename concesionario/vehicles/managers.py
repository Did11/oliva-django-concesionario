# vehicles/managers.py
from django.db import models
from django.db.models import Count

class VehicleManager(models.Manager):
    def hybrids(self):
        return self.filter(fuel_type='hybrid')

    def by_brand(self, brand_name):
        return self.filter(brand__name=brand_name)

    def without_images(self):
        return self.annotate(num_images=Count('images')).filter(num_images=0)
