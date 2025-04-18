# courses/serializers.py

from rest_framework import serializers
from courses.models import Course, Module, Step


class StepSerializer(serializers.ModelSerializer):
    class Meta:
        model = Step
        fields = [
            "id",
            "title",
            "description",
            "url_video",
            "url_image",
            "module_id",
            "created_at",
            "updated_at",
        ]
        read_only_fields = ["id", "created_at", "updated_at"]


class ModuleSerializer(serializers.ModelSerializer):
    steps = StepSerializer(many=True)

    class Meta:
        model = Module
        fields = ["id", "name", "description", "steps"]


class CourseSerializer(serializers.ModelSerializer):
    modules = ModuleSerializer(many=True, required=False)
    author_id = serializers.IntegerField()

    class Meta:
        model = Course
        fields = [
            "id",
            "title",
            "description",
            "image",
            "type",
            "value",
            "warranty_time",
            "total_hours",
            "total_classes",
            "students",
            "amount_students",
            "author_id",
            "modules",
        ]

    def create(self, validated_data):
        modules_data = validated_data.pop("modules", [])
        course = Course.objects.create(**validated_data)

        for module_data in modules_data:
            steps_data = module_data.pop("steps", [])
            module = Module.objects.create(course=course, **module_data)
            for step_data in steps_data:
                Step.objects.create(module=module, **step_data)

        return course


class ModuleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Module
        fields = ["id", "name", "description"]
