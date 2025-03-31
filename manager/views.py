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
    except models.About.DoesNotExist as err:
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
