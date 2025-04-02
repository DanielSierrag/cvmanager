from utils.phone_number_validaiton import choices as country_code_choices
from django.core.exceptions import ValidationError
from crispy_forms.layout import Layout, Field
from crispy_forms.helper import FormHelper
from datetime import datetime
import phonenumbers as pn
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


class ReferenceForm(forms.ModelForm):
    COUNTRY_CODES = country_code_choices

    country_code = forms.ChoiceField(
        help_text='+1 for USA',
        choices=COUNTRY_CODES
    )
    phone = forms.IntegerField(
        widget=forms.NumberInput(),
        required=True
    )

    class Meta:
        model = models.Reference
        fields = ['name', 'email']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            Field('country_code', css_class='form-select'),
            Field('phone', css_class='form-control m-1')
        )

    def clean(self):
        cleaned_data = super().clean()

        code = cleaned_data['country_code']
        try:
            phone = str(cleaned_data['phone'])
            is_valid = pn.is_valid_number(pn.parse(f"+{code}{phone}"))
            if not is_valid:
                self.add_error('phone', error=f'{phone} is not a valid number')
            else:
                phone = f"+{code} {phone}"
                cleaned_data['phone'] = phone
        except (KeyError, pn.NumberParseException):
            self.add_error('phone', error=f'Enter a valid number')

        return cleaned_data

    def save(self, commit=True):
        instance = super().save(commit=False)
        instance.phone = self.cleaned_data['phone']

        if commit:
            instance.save()

        return instance
