from django.contrib.auth.decorators import login_required, permission_required
from django.http import HttpResponse
from django.shortcuts import render
from . import models
from os import getenv

# Create your views here.


@login_required
def index(request):
    cv_list = models.CurriculumVitae.objects.filter(user=request.user)
    experiences_count = models.Experience.objects.count()
    return render(
        request,
        "manager/index.html",
        context={
            "cv_list": cv_list,
            "experiences_count": experiences_count,
        }
    )
