from django.urls import path
from courses.views import CourseView

urlpatterns = [
    path("courses/", CourseView.as_view()),
]