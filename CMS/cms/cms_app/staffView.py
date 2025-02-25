from django.shortcuts import render,redirect

def staff_home(request):
    return render(request,'staff_templates/staff_home.html')