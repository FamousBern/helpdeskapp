from django.forms import ModelForm
from .models import *
from django.contrib.auth.models import User



class ReportedDeviceForm(ModelForm):
    class Meta:
        model = ReportedDevices
        fields = ['device_type', 'device_serial', 'device_issue_description']
        exclude = ['device_origin', ]
