from django.db import models
from django.conf import settings
#Table for the patient
class Patient(models.Model):
    allowed_bloodtype=(
    ('A+','A+'),
    ('A-','A-'),
    ('B+','B+'),
    ('B-','B-'),
    ('AB+','AB+'),
    ('AB-','AB-'),
    )
    user=models.ForeignKey(settings.AUTH_USER_MODEL,default=0)
    aadhar_number=models.IntegerField(default=0)
    unique_number=models.CharField(max_length=20,default=0)
    first_name=models.CharField(max_length=30)
    last_name=models.CharField(max_length=30)
    phone_number=models.IntegerField()
    blood_type=models.CharField(max_length=4,choices=allowed_bloodtype)
    address=models.CharField(max_length=220)
    pincode=models.IntegerField()
    state=models.CharField(max_length=20)
    city=models.CharField(max_length=20)
    emergency_contact=models.IntegerField()
#Table for the Prescription
class Prescription(models.Model):
    allowed_medicines=(
    ('paracetomal','crocin-advance'),
    ('paracetomal','dolo'),

    )
    serialno=models.IntegerField()
    date_of_prescription=models.CharField(max_length=20,default='')
    doctors_name=models.CharField(max_length=20,default='')
    identifier=models.IntegerField(default=0)
    medicine_text=models.CharField(max_length=30,choices=allowed_medicines)
    dosage=models.CharField(max_length=20)
    quantity=models.IntegerField(default=0)
    consumption=models.CharField(max_length=20)
#Table for Report
class reports(models.Model):
    unique_number=models.ForeignKey(Patient,default=0)
    report_name=models.CharField(max_length=20,default='')
    report_date=models.CharField(max_length=20,default='')
    image_url=models.CharField(max_length=20,default=' ')
#Table for doctor
class doctor(models.Model):
    docuser=models.ForeignKey(settings.AUTH_USER_MODEL,default=0)
    aadhardoc=models.IntegerField()
    license=models.CharField(max_length=20)
    first_name=models.CharField(max_length=20)
    last_name=models.CharField(max_length=20)
    contact=models.IntegerField()
#Table for pharmacist
class pharmacist(models.Model):
    allowed_medicines=(
    ('paracetomal','crocin-advance'),
    ('paracetomal','dolo'),

    )
    pharmauser=models.ForeignKey(settings.AUTH_USER_MODEL,default=0)
    license=models.CharField(max_length=20)
    medicine_text=models.CharField(max_length=30,choices=allowed_medicines)
    quantity=models.IntegerField(default=0)
