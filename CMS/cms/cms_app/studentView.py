from django.shortcuts import render,redirect

def student_home(request):
    return render(request,'student_templates/student_home.html')