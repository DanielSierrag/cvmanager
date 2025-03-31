# Generated by Django 5.1.6 on 2025-03-30 17:15

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('manager', '0004_alter_about_desc'),
    ]

    operations = [
        migrations.AlterField(
            model_name='degree',
            name='entity',
            field=models.CharField(max_length=50, validators=[django.core.validators.MinLengthValidator(5, 'The content is too short')]),
        ),
        migrations.AlterField(
            model_name='degree',
            name='level',
            field=models.CharField(choices=[("BACHELOR's DEGREE", "BACHELOR's DEGREE"), ("ASOCIATE's DEGREE", "ASOCIATE's DEGREE"), ('DIPLOMATE', 'DIPLOMATE'), ('ESPECIALIZATION', 'ESPECIALIZATION')], max_length=30),
        ),
        migrations.AlterField(
            model_name='degree',
            name='title',
            field=models.CharField(max_length=50, validators=[django.core.validators.MinLengthValidator(5, 'The content is too short')]),
        ),
        migrations.AlterField(
            model_name='experience',
            name='desc',
            field=models.TextField(max_length=700, validators=[django.core.validators.MinLengthValidator(10, 'The content is too short')]),
        ),
        migrations.AlterField(
            model_name='experience',
            name='entity',
            field=models.CharField(max_length=50, validators=[django.core.validators.MinLengthValidator(5, 'The content is too short')]),
        ),
        migrations.AlterField(
            model_name='experience',
            name='role',
            field=models.CharField(max_length=30, validators=[django.core.validators.MinLengthValidator(5, 'The content is too short')]),
        ),
        migrations.AlterField(
            model_name='reference',
            name='name',
            field=models.CharField(max_length=50, validators=[django.core.validators.MinLengthValidator(3, 'The name must have at least 3 characters')]),
        ),
        migrations.AlterField(
            model_name='skill',
            name='name',
            field=models.CharField(max_length=15, validators=[django.core.validators.MinLengthValidator(3, 'The content is too short')]),
        ),
    ]
