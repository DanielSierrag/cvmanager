from .owner import OwnerCreateView, OwnerUpdateView, OwnerListView, OwnerDeleteView
from django.contrib.auth.decorators import login_required, permission_required
from django.http import HttpResponse
from django.shortcuts import render
from . import models
from . import forms
# Create your views here.


@login_required
def index(request):
    try:
        about = models.About.objects.get(user=request.user)
    except models.About.DoesNotExist:
        print('User does not have about related object')
        about = None

    return render(
        request,
        "manager/index.html",
        context={"about": about}
    )


class AboutCreateView(OwnerCreateView):
    model = models.About
    fields = ['desc']


class AboutUpdateView(OwnerUpdateView):
    model = models.About
    form_class = forms.AboutForm


# Epeciences section
class ExperienceListView(OwnerListView):
    model = models.Experience

    def get_queryset(self):
        qs = super().get_queryset()

        return qs.order_by("-id")


class ExperienceCreateView(OwnerCreateView):
    model = models.Experience
    form_class = forms.ExperienceForm


class ExperienceUpdateView(OwnerUpdateView):
    model = models.Experience
    form_class = forms.ExperienceForm


class ExperienceDeleteView(OwnerDeleteView):
    model = models.Experience
    template_name = "manager/item_confirm_delete.html"


# Education section
class EducationListView(OwnerListView):
    model = models.Education

    def get_queryset(self):
        qs = super().get_queryset()
        return qs.order_by('-id')


class EducationCreateView(OwnerCreateView):
    model = models.Education
    form_class = forms.EducationForm


class EducationUpdateView(OwnerUpdateView):
    model = models.Education
    form_class = forms.EducationForm


class EducationDeleteView(OwnerDeleteView):
    model = models.Education
    template_name = "manager/item_confirm_delete.html"


# Skills section
class SkillListView(OwnerListView):
    model = models.Skill

    def get_queryset(self):
        qs = super().get_queryset()
        return qs.order_by('-id')


class SkillCreateView(OwnerCreateView):
    model = models.Skill
    form_class = forms.SkillForm


class SkillUpdateView(OwnerUpdateView):
    model = models.Skill
    form_class = forms.SkillForm


class SkillDeleteView(OwnerDeleteView):
    model = models.Skill
    template_name = "manager/item_confirm_delete.html"


# References section
class ReferenceListView(OwnerListView):
    model = models.Reference

    def get_queryset(self):
        qs = super().get_queryset()
        return qs.order_by('-id')


class ReferenceCreateView(OwnerCreateView):
    model = models.Reference
    form_class = forms.ReferenceForm


class ReferenceUpdateView(OwnerUpdateView):
    model = models.Reference
    form_class = forms.ReferenceForm


class ReferenceDeleteView(OwnerDeleteView):
    model = models.Reference
    template_name = "manager/item_confirm_delete.html"
