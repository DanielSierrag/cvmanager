# Generated by Django 5.1.6 on 2025-03-28 22:07

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('manager', '0003_rename_degree_curriculumvitae_degrees_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='about',
            name='desc',
            field=models.TextField(max_length=800, validators=[django.core.validators.MinLengthValidator(20, 'The about section must have at least 20 characters')]),
        ),
    ]
