from django.urls import path

from .views import home_view, students_view

urlpatterns = [
    path('', home_view, name="home"),
    path('student/<int:pk>', students_view, name="student-detail")
]
