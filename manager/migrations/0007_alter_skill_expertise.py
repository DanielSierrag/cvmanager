# Generated by Django 5.1.6 on 2025-03-31 14:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('manager', '0006_rename_degree_education_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='skill',
            name='expertise',
            field=models.CharField(choices=[('BEGGINER', 'BEGGINER'), ('INTERMEDIATE', 'INTERMEDIATE'), ('ADVANCED', 'ADVANCED')], max_length=30),
        ),
    ]
