from rest_framework.views import APIView, status
from rest_framework.response import Response
from courses.models import Course
from django.forms.models import model_to_dict
from courses.serializers import CourseSerializer


# Create your views here.
class CourseView(APIView):
    def post(self, request):
        serializer = CourseSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        course_data = Course.objects.create(**serializer.validated_data)
        return Response(model_to_dict(course_data), status.HTTP_201_CREATED)

    def get(self, request):
        courses = Course.objects.all()
        courses_list = []

        for course in courses:
            courses_list.append(model_to_dict(course))

        return Response(
            {"data": courses_list, "message": "List of courses listed successfully"},
            status.HTTP_200_OK,
        )
