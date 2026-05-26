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

    student_name = models.CharField(max_length=200)

    project_domain = models.CharField(max_length=200)

    rating = models.IntegerField()

    review_text = models.TextField()

    improvement_text = models.TextField()

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
    

class Users(models.Model):

    name = models.CharField(max_length=200)

    email = models.EmailField(unique=True)

    password = models.CharField(max_length=200)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):

        return self.email
    

class Projecttitles(models.Model):

    title = models.CharField(max_length=300)

    DOMAIN_CHOICES = [

        ('VLSI', 'VLSI'),

        ('Embedded', 'Embedded'),

        ('IoT', 'IoT'),

        ('Software', 'Software')

    ]


    domain = models.CharField(

        max_length=200,

        choices=DOMAIN_CHOICES

    )

    technologies = models.CharField(max_length=500)

    description = models.TextField(blank=True,
        null=True)

    image = models.ImageField(upload_to='projects/', blank=True,
        null=True)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):

        return self.title



class ChatMessage(models.Model):

    username = models.CharField(
        max_length=200
    )

    message = models.TextField()

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):

        return self.username

# Create your models here.
