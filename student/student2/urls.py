from django.urls import path
from student2 import views as s2

urlpatterns = [
    path("" , s2.stu2_name)
]
