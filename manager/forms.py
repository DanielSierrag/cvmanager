from django.core.exceptions import ValidationError
from crispy_forms.layout import Layout, Field
from crispy_forms.helper import FormHelper
from datetime import datetime
from django import forms
from . import models
# Write your forms here


def date_validator(value):
    if value > datetime.now().date():
        raise ValidationError("Please enter a valid date")


class AboutForm(forms.ModelForm):
    class Meta:
        model = models.About
        fields = ['desc']
        widgets = {
            'desc': forms.Textarea(attrs={'class': 'form-control', 'style': 'height: 200px'}),
        }


class ExperienceForm(forms.ModelForm):
    since = forms.DateField(
        input_formats=["%Y-%m"],
        label="Since", required=True,
        widget=forms.DateInput(
            attrs={"type": "month", "class": "ms-1 form-control"}),
        validators=[date_validator]
    )
    until = forms.DateField(
        input_formats=["%Y-%m"],
        label="Until", required=False,
        widget=forms.DateInput(
            attrs={"type": "month", "class": "ms-1 form-control"}
        ),
        help_text="Leave blank if you're still working there",
        validators=[date_validator]
    )

    class Meta:
        model = models.Experience
        fields = ["role", "entity", "desc"]
        widgets = {
            "desc": forms.Textarea(attrs={"class": "form-control", "style": "height: 200px"})
        }

    def clean(self):
        cleaned_data = super().clean()
        since = self.cleaned_data.get("since")
        until = self.cleaned_data.get("until")
        if since and until:
            cleaned_data['timelapse'] = f"{since} to {until}"
        elif since and not until:
            cleaned_data['timelapse'] = f"{since} to present"

        return cleaned_data

    def save(self, commit=True):
        instance = super().save(commit=False)
        instance.timelapse = self.cleaned_data.get('timelapse', '')

        if commit:
            instance.save()

        return instance


class EducationForm(forms.ModelForm):
    since = forms.DateField(
        input_formats=["%Y-%m"],
        label="Since", required=True,
        widget=forms.DateInput(
            attrs={"type": "month", "class": "ms-1 form-control"}),
        validators=[date_validator]
    )
    until = forms.DateField(
        input_formats=["%Y-%m"],
        label="Until", required=False,
        widget=forms.DateInput(
            attrs={"type": "month", "class": "ms-1 form-control"}
        ),
        help_text="Leave blank if you're still studying there",
        validators=[date_validator]
    )

    class Meta:
        model = models.Education
        fields = ["level", "entity", "title"]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            Field('level', css_class='form-select')
        )

    def clean(self):
        cleanned_data = super().clean()
        since = cleanned_data.get('since')
        until = cleanned_data.get('until')

        if since and until:
            cleanned_data['timelapse'] = f"{since} to {until}"
        elif since and not until:
            cleanned_data['timelapse'] = f"{since} to present"

        return cleanned_data

    def save(self, commit=True):
        instance = super().save(commit=False)
        instance.timelapse = self.cleaned_data.get('timelapse', '')

        if commit:
            instance.save()

        return instance


class SkillForm(forms.ModelForm):
    class Meta:
        model = models.Skill
        fields = ["name", "expertise"]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            Field('expertise', css_class='form-select')
        )
