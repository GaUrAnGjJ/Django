from django.urls import path,include
from student1 import views as s1

urlpatterns = [
    path('',s1.student_age ),
    path('name/' , s1.student_name)
]