from django.db import models


# Create your models here.
class Course(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    image = models.URLField()
    type = models.CharField(max_length=50)
    value = models.DecimalField(max_digits=10, decimal_places=2)
    warranty_time = models.IntegerField()  # em dias
    total_hours = models.IntegerField()
    total_classes = models.IntegerField()
    students = models.IntegerField()
    amount_students = models.IntegerField()
    author = models.ForeignKey(
        "accounts.User", on_delete=models.CASCADE, related_name="courses"
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Module(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    course = models.ForeignKey(
        "Course", on_delete=models.CASCADE, related_name="modules"
    )

    def __str__(self):
        return self.name


class Step(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    url_video = models.URLField()
    url_image = models.URLField()
    module = models.ForeignKey(
        "courses.Module", on_delete=models.CASCADE, related_name="steps"
    )

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
