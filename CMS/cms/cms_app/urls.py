from django.urls import path
from . import views, studentView, hodView, staffView

urlpatterns = [
    path('', views.home_view, name='home'),

    #authentication
    path('login/',views.login_view, name='login'),
    path('register/', views.register, name='register'),
    path('logout/', views.logout_view, name='logout'),



    #students
    path('student_home/', studentView.student_home, name='student_home'),


    #HOD
    path('hod_home/', hodView.hod_home, name='hod_home'),
    path('hod_add_course/', hodView.manage_course_view, name='manage_course_view'),
    path('delete_course/<int:id>', hodView.delete_course, name='delete_course'),
    path('edit_course/<int:id>', hodView.edit_course, name='edit_course'),

    path('manage_subject/', hodView.manage_subject_view, name='manage_subject_view'),

    path('hod_manage_staff/', hodView.manage_staff_view, name='manage_staff_view'),
    path('hod_add_staff/',hodView.add_staff_view, name='add_staff_view'),
    path('delet_staff/<int:id>', hodView.delete_staff, name='delete_staff'),
    path('edit_staff/', hodView.edit_staff, name='edit_staff'),


    #staff
    path('staff_home/', staffView.staff_home, name='staff_home'),
]