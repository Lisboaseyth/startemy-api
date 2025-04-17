from rest_framework.views import APIView, status
from rest_framework.response import Response
from rest_framework.pagination import PageNumberPagination
from courses.models import Course
from courses.serializers import CourseSerializer


# Create your views here.
class CourseView(APIView, PageNumberPagination):

    def post(self, request):
        serializer = CourseSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        course = Course.objects.create(**serializer.validated_data)
        serializer = CourseSerializer(course)
        return Response(serializer.data, status.HTTP_201_CREATED)

    def get(self, request):
        type_param = request.query_params.get("type")
        id_param = request.query_params.get("id")

        if id_param:
            courses_list = Course.objects.filter(id=id_param)
        elif type_param:
            courses_list = Course.objects.filter(type__iexact=type_param)
        else:
            courses_list = Course.objects.all()

        result_page = self.paginate_queryset(courses_list, request, view=self)

        serializer = CourseSerializer(result_page, many=True)

        return self.get_paginated_response(
            {
                "data": serializer.data,
                "message": "List of courses listed successfully",
            }
        )
