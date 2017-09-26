from django import forms
from .models import Patient,Prescription
#ModelForms for Signup and Presc
class Signup(forms.ModelForm):
    class Meta:
        model=Patient
        fields=['aadhar_number','unique_number','first_name','last_name','phone_number','blood_type','address','pincode'
        ,'state','city','emergency_contact']
class Presc(forms.ModelForm):
        class Meta:
            model=Prescription
            fields=['medicine_text','quantity']
