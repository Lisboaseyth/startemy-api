from django.urls import path
from courses.views import (
    CourseView,
    CourseModuleView,
    CourseDetailView,
    ModuleDetailView,
    StepCreateView,
    StepDetailView,
    StepListCreateView,
)

urlpatterns = [
    path("courses/", CourseView.as_view()),
    path("courses/<int:course_id>/", CourseDetailView.as_view()),
    path("courses/<int:course_id>/modules/", CourseModuleView.as_view()),
    path(
        "courses/<int:course_id>/modules/<int:module_id>/", ModuleDetailView.as_view()
    ),
    path(
        "courses/<int:course_id>/modules/<int:module_id>/steps/",
        StepListCreateView.as_view(),
    ),
    path(
        "courses/<int:course_id>/modules/<int:module_id>/steps/<int:step_id>/",
        StepDetailView.as_view(),
    ),
]
