from django.contrib import admin

# Register your models here.
from .models import Patient,Prescription,reports,doctor,pharmacist
# Register your models here.
admin.site.register(Patient)
admin.site.register(Prescription)
admin.site.register(reports)
admin.site.register(doctor)
admin.site.register(pharmacist)
