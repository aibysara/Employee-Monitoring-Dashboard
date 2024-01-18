from django.db import models

# Create your models here.
from django.contrib.auth.models import User


mode_status=[('Offline', 'Offline'), ('Online', 'Online')]

class Employee(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_pic = models.ImageField(upload_to='profile_pic/EmployeeProfilePic/', null=True, blank=True)
    mode = models.CharField(max_length=128, choices=mode_status, default='Offline')
    address = models.CharField(max_length=128)
    mobile = models.CharField(max_length=12, null=True)
    email = models.EmailField(max_length=128, null=True)
    status = models.BooleanField(default=False)
    last_activity = models.DateTimeField(null=True, blank=True)

    @property
    def get_name(self):
        return self.user.first_name + " " + self.user.last_name

    @property
    def get_id(self):
        return self.user.id

    def __str__(self):
        return f"{self.user.first_name} - {'Online' if self.status else 'Offline'}"

