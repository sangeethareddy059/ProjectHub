from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Project(models.Model):

    PROJECT_TYPES = (
        ('hardware', 'Hardware'),
        ('software', 'Software'),
    )

    title = models.CharField(max_length=200)

    project_type = models.CharField(
        max_length=20,
        choices=PROJECT_TYPES
    )

    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE
    )

    description = models.TextField()

    advantages = models.TextField()

    implementation = models.TextField()

    image = models.ImageField(
        upload_to='projects/'
    )

    video = models.FileField(
        upload_to='videos/',
        blank=True,
        null=True
    )

    abstract_pdf = models.FileField(
        upload_to='abstracts/'
    )

    report_pdf = models.FileField(
        upload_to='reports/'
    )

    ppt_file = models.FileField(
        upload_to='ppts/'
    )

    source_code = models.FileField(
        upload_to='sourcecodes/',
        blank=True,
        null=True
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):
        return self.title


class Contact(models.Model):

    name = models.CharField(max_length=100)

    email = models.EmailField()

    phone = models.CharField(max_length=20)

    message = models.TextField()

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):
        return self.name

class Reviews(models.Model):

    name = models.CharField(max_length=100)

    feedback = models.TextField()

    rating = models.IntegerField(default=5)

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):
        return self.name


# Create your models here.
