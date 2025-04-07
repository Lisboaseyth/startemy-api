from rest_framework import serializers


class CourseSerializer(serializers.Serializer):
    title = serializers.CharField()
    description = serializers.CharField()
    image = serializers.URLField()
    type = serializers.CharField(max_length=50)
    value = serializers.DecimalField(max_digits=10, decimal_places=2)
    warranty_time = serializers.IntegerField()
    total_hours = serializers.IntegerField()
    total_classes = serializers.IntegerField()
    students = serializers.IntegerField()
    amount_students = serializers.IntegerField()
    author_id = serializers.IntegerField()
