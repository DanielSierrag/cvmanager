from django.urls import path, reverse_lazy
from . import views

app_name = "manager"

urlpatterns = [
    path("", views.index, name="index"),
    path(
        "about/create",
        views.AboutCreateView.as_view(
            success_url=reverse_lazy("manager:index")),
        name="about_create"
    ),
    path(
        "about/<int:pk>/update",
        views.AboutUpdateView.as_view(
            success_url=reverse_lazy("manager:index")),
        name="about_update"
    ),
    path(
        "experiences",
        views.ExperienceListView.as_view(),
        name="experience_list"
    ),
    path(
        "experience/create",
        views.ExperienceCreateView.as_view(
            success_url=reverse_lazy("manager:experience_list")),
        name="experience_create"
    ),
    path(
        "experience/<int:pk>/update",
        views.ExperienceUpdateView.as_view(
            success_url=reverse_lazy("manager:experience_list")),
        name="experience_update"
    ),
    path(
        "experience/<int:pk>/delete",
        views.ExperienceDeleteView.as_view(
            success_url=reverse_lazy("manager:experience_list")),
        name="experience_delete"
    ),
    path(
        "educations",
        views.EducationListView.as_view(),
        name="education_list"
    ),
    path(
        "education/create",
        views.EducationCreateView.as_view(
            success_url=reverse_lazy("manager:education_list")),
        name="education_create"
    ),
    path(
        "education/<int:pk>/update",
        views.EducationUpdateView.as_view(
            success_url=reverse_lazy("manager:education_list")),
        name="education_update"
    ),
    path(
        "education/<int:pk>/delete",
        views.EducationDeleteView.as_view(
            success_url=reverse_lazy("manager:education_list")),
        name="education_delete"
    ),
]
