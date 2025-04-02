from django.core import validators
from django.conf import settings
from django.db import models

# Create your models here.


class UserDemographic(models.Model):
    STATUSES = [
        ("FREELANCER", "FREELANCER"),
        ("EMPLOYED", "EMPLOYED"),
        ("OPEN TO  WORK", "OPEN TO  WORK"),
        ("OPEN TO INTERVIEWS", "OPEN TO INTERVIEWS"),
    ]
    invalid_message = 'The content is too short'

    avatar = models.ImageField(upload_to="media/user/avatars")
    adress = models.CharField(
        max_length=20,
        validators=[validators.MinLengthValidator(3, invalid_message)]
    )
    phone = models.CharField(
        max_length=30,
    )
    profession = models.CharField(
        max_length=20,
        validators=[validators.MinLengthValidator(3, invalid_message)]
    )
    status = models.CharField(max_length=50, choices=STATUSES)

    user = models.OneToOneField(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.user.username}\'s info'


class SocialMedia(models.Model):
    SOCIALS = [
        ("LinkedIn", "LinkedIn"),
        ("x/Twitter", "x/Twitter"),
        ("Facebook", "facebook"),
        ("Portfolio", "portfolio"),
    ]
    name = models.CharField(max_length=20, choices=SOCIALS)
    url = models.URLField()
    user_data = models.ForeignKey(
        UserDemographic,
        on_delete=models.CASCADE,
        related_name='user_socials'
    )

    def __str__(self):
        return self.name


class Experience(models.Model):
    minlen_message = "The content is too short"

    role = models.CharField(max_length=30, null=False, validators=[
                            validators.MinLengthValidator(5, minlen_message)])
    entity = models.CharField(max_length=50, null=False, validators=[
                              validators.MinLengthValidator(5, minlen_message)])
    desc = models.TextField(max_length=700, null=False, validators=[
                            validators.MinLengthValidator(10, minlen_message)])
    timelapse = models.CharField(max_length=25, null=False)
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.role} in {self.entity}"


class Education(models.Model):
    LEVELS = [
        ("BACHELOR's DEGREE", "BACHELOR's DEGREE"),
        ("ASOCIATE's DEGREE", "ASOCIATE's DEGREE"),
        ("DIPLOMATE", "DIPLOMATE"),
        ("ESPECIALIZATION", "ESPECIALIZATION"),
    ]
    minlen_message = "The content is too short"

    level = models.CharField(choices=LEVELS, max_length=30, null=False)
    entity = models.CharField(max_length=50, null=False, validators=[
                              validators.MinLengthValidator(5, minlen_message)])
    title = models.CharField(max_length=50, null=False, validators=[
                             validators.MinLengthValidator(5, minlen_message)])
    timelapse = models.CharField(max_length=25, null=False)
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.title} {self.level}"


class Skill(models.Model):
    EXPERTISE = [
        ("BEGGINER", "BEGGINER"),
        ("INTERMEDIATE", "INTERMEDIATE"),
        ("ADVANCED", "ADVANCED"),
    ]

    name = models.CharField(max_length=15, null=False, validators=[
                            validators.MinLengthValidator(3, "The content is too short")])
    expertise = models.CharField(choices=EXPERTISE, max_length=30, null=False)
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} skill"


class About(models.Model):
    desc = models.TextField(max_length=800, validators=[validators.MinLengthValidator(
        20, 'The about section must have at least 20 characters')])
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username}'s profile"


class Reference(models.Model):
    name = models.CharField(
        max_length=50, null=False,
        validators=[
            validators.MinLengthValidator(3, "The name must have at least 3 characters")]
    )
    phone = models.CharField(
        max_length=30,
        null=False,
        help_text="Just numbers, not spaces or special characters"
    )
    email = models.EmailField(blank=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Template(models.Model):
    CATEGORIES = [
        ("FORMAL", "FORMAL"),
        ("MINIMALIST", "MINIMALIST"),
    ]

    name = models.CharField(
        max_length=30, blank=False,
        null=False
        # null=False, unique=True
    )
    category = models.CharField(choices=CATEGORIES, max_length=30, null=False)
    file = models.FileField(
        upload_to="media/templates/",
        blank=False,
        null=False
    )
    creted_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class CurriculumVitae(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             on_delete=models.CASCADE)
    experiences = models.ManyToManyField(Experience)
    educations = models.ManyToManyField(Education)
    skills = models.ManyToManyField(Skill)
    about = models.OneToOneField(About, on_delete=models.CASCADE)
    references = models.ManyToManyField(Reference)
    template = models.OneToOneField(Template, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username}'s cv"
