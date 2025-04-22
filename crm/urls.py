from django.urls import path

from crm import views

urlpatterns=[
    path("students/",views.StudentLiscreatetView.as_view()),
    path("students/<int:pk>/",views.StudentRetrieveUpdateDestroyView.as_view()),

]