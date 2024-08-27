# media/models.py

import os
from uuid import uuid4
from django.db import models
from vehicles.models import Vehicle

def get_file_path(instance, filename):
    """
    Generates a unique filename and stores it in a specific subdirectory for each vehicle
    under the '/vehicle_images/uploads/{vehicle_id}/' directory.
    """
    # Extract the file extension, e.g., '.jpg'
    extension = os.path.splitext(filename)[1]
    # Generate a new unique filename using UUID
    new_filename = f"{uuid4().hex}{extension}"
    # Combine with the destination directory specific to the vehicle under '/vehicle_images/uploads/{instance.vehicle.id}/'
    return os.path.join(f'vehicle_images/uploads/{instance.vehicle.id}/', new_filename)

# Model for storing vehicle images
class VehicleImage(models.Model):
    vehicle = models.ForeignKey(Vehicle, related_name='images', on_delete=models.CASCADE)
    image = models.ImageField(upload_to=get_file_path)
    is_main = models.BooleanField(default=False)  # Indicates if this image is the main cover

    def __str__(self):
        return f"Image for {self.vehicle.model}"
