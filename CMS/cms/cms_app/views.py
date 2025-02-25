from django.shortcuts import render,redirect
from django.contrib import messages
from .models import *
from django.contrib.auth import logout, authenticate, login
# Create your views here.



def home_view(request):
    return render(request, 'home.html')



def login_view(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')

        if not (email and password):
            messages.error(request, "Please provide all the details!!")
            return render(request, 'login.html')

        user = CustomUser.objects.filter(email=email, password=password).last()

        if not user:
            messages.error(request, 'Invalid Login Credentials!!')
            return render(request, 'login.html')

        login(request, user)

        if user.user_type == CustomUser.STUDENT:
            return redirect('student_home')
        elif user.user_type == CustomUser.STAFF:
            return redirect('staff_home')
        elif user.user_type == CustomUser.HOD:
            return redirect('hod_home')

    return render(request, 'login.html')


def register(request):
    if request.method == 'POST':
        first_name = request.POST.get('first_name')
        username = request.POST.get('username')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')

        if not(
                first_name and
                last_name and
                username and
                email and
                password and
                confirm_password and
                confirm_password
        ):
            messages.error(request, 'Please enter all the fields')
            return render(request, 'register.html')

        if password != confirm_password:
            messages.error(request, 'Passwords do not match')
            return render(request, 'register.html')

        user = CustomUser.objects.filter(email=email).exists()
        if user:
            messages.error(request, 'Email already registered')
            return render(request, 'register.html')

        user_type = get_user_type_from_email(email)

        if user_type is None:
            messages.error(request, "Invalid email eg.'<username>.<staff|student|hod>@<college_domain>'")
            return render(request, 'register.html')

        new_user = CustomUser()
        new_user.first_name = first_name
        new_user.last_name = last_name
        new_user.username = username
        new_user.email = email
        new_user.password = password
        new_user.user_type = user_type
        new_user.save()

        if user_type == CustomUser.STAFF:
            Staff.objects.create(user=new_user)
        elif user_type == CustomUser.HOD:
            HOD.objects.create(user=new_user)
        elif user_type == CustomUser.STUDENT:
            Student.objects.create(user=new_user)

        return render(request, 'login.html')

    return render(request, 'register.html')


def logout_view(request):
    logout(request)
    return redirect('login')


def get_user_type_from_email(email):
    # Dummy implementation - Replace with actual logic
    if "staff" in email:
        return CustomUser.STAFF
    elif "hod" in email:
        return CustomUser.HOD
    elif "student" in email:
        return CustomUser.STUDENT
    return None