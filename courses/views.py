from rest_framework.views import APIView, status
from rest_framework.response import Response
from rest_framework.pagination import PageNumberPagination
from courses.models import Course, Module, Step
from courses.serializers import CourseSerializer, ModuleSerializer, StepSerializer
from django.shortcuts import get_object_or_404
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
from rest_framework.exceptions import PermissionDenied


# Create your views here.
class CourseView(APIView, PageNumberPagination):
    permission_classes = [IsAuthenticatedOrReadOnly]

    def post(self, request):
        serializer = CourseSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        course = Course.objects.create(author=request.user, **serializer.validated_data)
        serializer = CourseSerializer(course)
        return Response(
            {"data": serializer.data, "message": "Course created sucessfully"},
            status.HTTP_201_CREATED,
        )

    def get(self, request):
        type_param = request.query_params.get("type")
        id_param = request.query_params.get("id")

        if id_param:
            course = get_object_or_404(Course, id=id_param)
            serializer = CourseSerializer(course)
            return Response(serializer.data)

        if type_param:
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


class CourseDetailView(APIView):
    permission_classes = [IsAuthenticated]

    def patch(self, request, course_id):
        course = get_object_or_404(Course, id=course_id)

        if request.user != course.author:
            return Response(
                {"detail": "Permission denied."}, status=status.HTTP_403_FORBIDDEN
            )

        serializer = CourseSerializer(course, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(
            {"data": serializer.data, "message": "Course updated sucessfully"},
            status=status.HTTP_200_OK,
        )

    def delete(self, request, course_id):
        course = get_object_or_404(Course, id=course_id)

        if request.user != course.author:
            return Response(
                {"detail": "Permission denied."}, status=status.HTTP_403_FORBIDDEN
            )

        course.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class CourseModuleView(APIView, PageNumberPagination):
    permission_classes = [IsAuthenticatedOrReadOnly]

    def get(self, request, course_id):
        course = get_object_or_404(Course, id=course_id)
        modules = Module.objects.filter(course=course)
        results = self.paginate_queryset(modules, request, view=self)
        serializer = ModuleSerializer(results, many=True)
        return self.get_paginated_response(
            {"data": serializer.data, "message": "Modules retrieved successfully"}
        )

    def post(self, request, course_id):
        course = get_object_or_404(Course, id=course_id)

        if course.author != request.user:
            raise PermissionDenied(
                "Você não tem permissão para adicionar módulos a este curso."
            )

        serializer = ModuleSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save(course=course)

        return Response(
            {"data": serializer.data, "message": "Module created successfully"},
            status=status.HTTP_201_CREATED,
        )


class ModuleDetailView(APIView):
    permission_classes = [IsAuthenticated]

    def patch(self, request, course_id, module_id):
        course = get_object_or_404(Course, id=course_id)
        module = get_object_or_404(Module, id=module_id, course=course)

        if request.user != course.author:
            return Response(
                {"detail": "Permission denied."}, status=status.HTTP_403_FORBIDDEN
            )

        serializer = ModuleSerializer(module, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(serializer.data, status=status.HTTP_200_OK)

    def delete(self, request, course_id, module_id):
        course = get_object_or_404(Course, id=course_id)
        module = get_object_or_404(Module, id=module_id, course=course)

        if request.user != course.author:
            return Response(
                {"detail": "Permission denied."}, status=status.HTTP_403_FORBIDDEN
            )

        module.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class StepListCreateView(APIView, PageNumberPagination):
    permission_classes = [IsAuthenticated]

    def get(self, request, course_id, module_id):
        course = get_object_or_404(Course, id=course_id)
        module = get_object_or_404(Module, id=module_id, course=course)

        steps = Step.objects.filter(module=module)
        results = self.paginate_queryset(steps, request, view=self)
        serializer = StepSerializer(results, many=True)

        return self.get_paginated_response(serializer.data)

    def post(self, request, course_id, module_id):
        course = get_object_or_404(Course, id=course_id)
        module = get_object_or_404(Module, id=module_id, course=course)

        if course.author != request.user:
            return Response(
                {"detail": "Você não tem permissão para adicionar steps neste módulo."},
                status=status.HTTP_403_FORBIDDEN,
            )

        serializer = StepSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save(module=module)

        return Response(serializer.data, status=status.HTTP_201_CREATED)


class StepDetailView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, course_id, module_id, step_id):
        course = get_object_or_404(Course, id=course_id)
        module = get_object_or_404(Module, id=module_id, course=course)
        step = get_object_or_404(Step, id=step_id, module=module)

        serializer = StepSerializer(step)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def patch(self, request, course_id, module_id, step_id):
        course = get_object_or_404(Course, id=course_id)
        module = get_object_or_404(Module, id=module_id, course=course)
        step = get_object_or_404(Step, id=step_id, module=module)

        if course.author != request.user:
            return Response(
                {"detail": "Você não tem permissão para editar este step."},
                status=status.HTTP_403_FORBIDDEN,
            )

        serializer = StepSerializer(step, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(serializer.data, status=status.HTTP_200_OK)

    def delete(self, request, course_id, module_id, step_id):
        course = get_object_or_404(Course, id=course_id)
        module = get_object_or_404(Module, id=module_id, course=course)
        step = get_object_or_404(Step, id=step_id, module=module)

        if course.author != request.user:
            return Response(
                {"detail": "Você não tem permissão para deletar este step."},
                status=status.HTTP_403_FORBIDDEN,
            )

        step.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
