from django.shortcuts import render,redirect
from .form import *

def hod_home(request):
    courses = Course.objects.all()
    staffs = CustomUser.objects.filter(user_type=CustomUser.STAFF)

    total_courses = courses.count()
    total_staffs = staffs.count()

    context = {
        'total_courses': total_courses,
        'total_staffs': total_staffs,
    }
    return render(request,'hod_templates/hod_home.html', context)


def manage_course_view(request):
    courses = Course.objects.all()

    if request.method == "POST":
        form = CourseForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('manage_course_view')
    else:
        form = CourseForm()

    context = {
        'form': form,
        'courses': courses
    }
    return render(request, 'hod_templates/hod_add_course.html', context)


def delete_course(request, id):
    course = Course.objects.get(id=id)
    if request.method == "POST":
        course.delete()
        return redirect('manage_course_view')

    context = {
        'course': course
    }
    return render(request,'hod_templates/delete_course.html', context)


def edit_course(request, id):
    course = Course.objects.get(id=id)
    if request.method == "POST":
        form = CourseForm(request.POST, instance=course)
        if form.is_valid():
            form.save()
            return redirect('manage_course_view')
    else:
        form = CourseForm(instance=course)

        context = {
            'form': form,
        }
        return render(request, 'hod_templates/edit_course.html', context)


def manage_subject_view(request):
    if request.method == "POST":
        form = SubjectForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('manage_subject_view')
    else:
        form = SubjectForm()
    context = {
        'form': form
    }
    return render(request,'hod_templates/manage_subject.html', context)


def manage_staff_view(request):
    staffs = CustomUser.objects.filter(user_type=CustomUser.STAFF)
    context = {
        'staffs': staffs,

    }
    return render(request, 'hod_templates/manage_staff.html', context)

def add_staff_view(request):
    form = UserCreationFrom()
    if request.method == 'POST':
        form = UserCreationFrom(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.is_staff = True
            CustomUser.objects.create(
                user = user
            )
    context = {
        'form': form
    }
    return render(request, 'hod_templates/add_staff.html',context)


def delete_staff(request, id):
    staff = Staff.objects.get(id=id)
    if request.method == "POST":
        staff.delete()
        return redirect('manage_staff_view')

    context = {
        'staff': staff
    }

    return render(request, 'hod_templates/delete_staff.html', context)


def edit_staff(request, id):

    return render(request, 'hod_templates/edit_staff.html' )