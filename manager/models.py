from django.db import models
from django.contrib.auth.models import User
from django.core import validators

# Create your models here.


class ProfileUser(User):
    avatar = models.ImageField(upload_to="media/user/avatars")
    user = models.ForeignKey(
        to=User, on_delete=models.CASCADE,
        related_name="profile"
    )


class Experience(models.Model):
    role = models.CharField(max_length=30, null=False)
    entity = models.CharField(max_length=50, null=False)
    desc = models.TextField(max_length=200, null=False)
    timelapse = models.CharField(max_length=25, null=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)


class Degree(models.Model):
    LEVELS = [
        ("DEGREE", "DEGREE"),
    ]

    level = models.CharField(choices=LEVELS, max_length=30, null=False)
    entity = models.CharField(max_length=50, null=False)
    title = models.CharField(max_length=50, null=False)
    timelapse = models.CharField(max_length=25, null=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)


class Skill(models.Model):
    EXPERTISE = [
        ("LOW", "LOW"),
        ("INTERMEDIATE", "INTERMEDIATE"),
        ("ADVANCED", "ADVANCED"),
    ]

    name = models.CharField(max_length=15, null=False)
    expertise = models.CharField(choices=EXPERTISE, max_length=30, null=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)


class About(models.Model):
    desc = models.TextField(max_length=200)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)


class Reference(models.Model):
    name = models.CharField(max_length=50, null=False)
    phone = models.IntegerField(
        null=False,
        validators=[validators.MaxValueValidator(9999999999999)],
        blank=True
    )
    email = models.EmailField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)


class Template(models.Model):
    CATEGORIES = [
        ("FORMAL", "FORMAL"),
        ("MINIMALIST", "MINIMALIST"),
    ]

    name = models.CharField(max_length=30, blank=False, null=False)
    category = models.CharField(choices=CATEGORIES, max_length=30, null=False)
    file = models.FileField(
        upload_to="media/templates/",
        blank=False,
        null=False
    )
    creted_at = models.DateTimeField(auto_now_add=True)


class CurriculumVitae(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    experience = models.ManyToManyField(Experience)
    degree = models.ManyToManyField(Degree)
    skill = models.ManyToManyField(Skill)
    about = models.OneToOneField(About, on_delete=models.CASCADE)
    references = models.ManyToManyField(Reference)
    template = models.OneToOneField(Template, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
