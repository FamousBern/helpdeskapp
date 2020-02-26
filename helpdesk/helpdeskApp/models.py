from django.conf import settings
from django.contrib.auth.models import User
from django.db import models


# Create your models here.
class NewDevices(models.Model):
    device_name = models.CharField(max_length=30, help_text='Specify device i.e mouse')
    device_serial_num = models.CharField(max_length=30, help_text='Add device serial number')
    device_model = models.CharField(max_length=30, help_text='Add model i.e HP')
    origin = models.ForeignKey(User, on_delete=models.CASCADE)
    device_status = models.CharField(max_length=30, help_text='Add deveice status i.e new or refurbished')
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Add All New Devices"

    def __str__(self): 
        return self.device_name


class ReportedDevices(models.Model):
    device_type = models.CharField(max_length=30)
    device_serial = models.CharField(max_length=30)
    # device_origin = models.CharField(max_length=30)
    device_origin = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    device_issue_description = models.TextField()
    date_reported = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "View all Reported Issues"

    def __str__(self):
        self.device_type


