from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class CustomUser(AbstractUser):
    HOD = '1'
    STAFF = '2'
    STUDENT = '3'

    EMAIL_TO_USE_ROLE = {
        'hod': HOD,
        'staff': STAFF,
        'student': STUDENT,
    }

    user_type_date = (
        (HOD, 'HOD')
        , (STAFF, 'STAFF')
        , (STUDENT, 'STUDENT')
    )

    user_type = models.CharField(default=1, choices=user_type_date, max_length=15)


class HOD(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    address = models.CharField(max_length=120)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Staff(models.Model):

    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, related_name='staff', null=True, blank=True)
    address = models.TextField(max_length=120, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True,null=True,blank=True)
    updated_at = models.DateTimeField(auto_now=True,null=True,blank=True)
    objects = models.Manager()


class Student(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    gender = models.CharField(max_length=50)
    profile_pic = models.FileField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Course(models.Model):
    course_name = models.CharField(max_length=50)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.course_name


class Subject(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    subject_name = models.CharField(max_length=50)
    staff_name =models.ForeignKey(Staff, on_delete=models.CASCADE)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)

    def __str__(self):
        return self.subject_name


