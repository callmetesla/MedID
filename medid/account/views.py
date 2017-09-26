from django.shortcuts import render,HttpResponse
from django.template import loader
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from .models import Patient,Prescription,reports
from subprocess import call
from .forms import Signup,Presc
#Index is used to signup users based on input data
#Routine still under development
def index(request):
    if request.method=='POST':
        form=SignupPatient(request.POST)
        if form.is_valid():
            first_name=form.cleaned_data['first_name']
            phone_number=form.cleaned_data['phone_number']
            password=form.cleaned_data['password']
            username=form.cleaned_data['username']
            user=User.create_user(username,password=password)
            user.save()
            user_login=authenticate(request,username=username,password=password)
            if user_login is not None:
                login(request,user)
                return HttpResponseRedirect('/')
            else:
                return HttpResponseRedirect("Error")
            if request.user.is_authenticated:
                return HttpResponseRedirect("/")
                form_signup=SignupPatient
                return render(request,'/account/index.html',{'f_signup':form_signup})
#View def for patient
def patientpage(request):
    #Check the RFID inputs
    fil=open('/home/callmetesla/Desktop/uid.txt','r')
    uniqueid=[]
    for line in fil:
        uniqueid.append(line.rstrip())
    fil.close()
    if not uniqueid:
        return render(request,'/account/')
    else:
        pat=Patient.objects.get(unique_number=uniqueid[-1])
        context={'pat':pat}
        return render(request,'account/profile_user.html',context)

def prescriptions_user(request):
    #Routine for prescriptions view for user
    fil=open('/home/callmetesla/Desktop/uid.txt','r')
    uniqueid=[]
    for line in fil:
        uniqueid.append(line.rstrip())
    fil.close()
    if not uniqueid:
        return render(request,'/account/')
    else:
        pat=Patient.objects.get(unique_number=uniqueid[-1])
        aadhar=pat.aadhar_number
        fin=Prescription.objects.filter(identifier=aadhar)
        s=fin.order_by('serialno')
        l={}
        m={}
        for x in s:
            m[x]=x
            l.update(m)
        context={'shiz':s}
        return render(request,'account/prescriptions_user.html',context)

def report_user(request):
    return render(request,'account/report_user.html')
def profile_doc(request):
    return render(request,'account/profile_doc.html')
def scan_doc(request):
    return render(request,'account/scan_doc.html')
def doc_view(request):
    fil=open('/home/callmetesla/Desktop/uid.txt','r')
    uniqueid=[]
    for line in fil:
        uniqueid.append(line.rstrip())
    fil.close()
    if not uniqueid:
        return render(request,'/account/profile_doc')
    else:
        print(uniqueid[-1])
        pat=Patient.objects.get(unique_number=uniqueid[-1])
        print(pat)
        context={'pat':pat}
        return render(request,'account/doc_view.html',context)
def doc_view_presc(request):
    fil=open('/home/callmetesla/Desktop/uid.txt','r')
    uniqueid=[]
    for line in fil:
        uniqueid.append(line.rstrip())
    fil.close()
    if not uniqueid:
        return render(request,'/account/')
    else:
        pat=Patient.objects.get(unique_number=uniqueid[-1])
        aadhar=pat.aadhar_number
        print(aadhar)
        fin=Prescription.objects.filter(identifier=aadhar)
        s=fin.order_by('serialno')
        l={}
        m={}
        for x in s:
            m[x]=x
            l.update(m)
        context={'shiz':s}
        return render(request,'account/doc_view_presc.html',context)
def report_doc(request):
    return render(request,'account/report_doc.html')
def trial(request):
    forma=Signup(request.POST)
    if request.method=='POST':
        forma=Signup(request.POST)
        if forma.is_valid():
            forma.save()
            return HttpResponseRedirect('/')
        else:
            forma=Signup()
    return render(request,'account/signup.html',{'forma':forma})
def doc_presc_new(request):
    form=Presc(request.POST)
    if form.is_valid():
        form.save()
        return HttpResponseRedirect('account/doc_view_presc.html')
    else:
        form=Presc()
    return render(request,'account/doc_presc_new.html',{'form':form})
def profile_pharm(request):
    return render(request,'account/profile_pharm.html')
def scand(request):
    return render(request,'account/scand.html')
def login(request):
    return render(request,'account/login.html')
def login_doc(request):
    return render(request,'account/login_doc.html')
def login_phar(request):
    return render(request,'account/login_phar.html')
