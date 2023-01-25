# Generated by Django 4.1.4 on 2023-01-19 11:38

import curs_manager.models
import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('curs_manager', '0008_alter_student_cnp'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='cnp',
            field=models.CharField(blank=True, max_length=13, null=True, unique=True, validators=[django.core.validators.MinLengthValidator(13), curs_manager.models.validate_no_a, curs_manager.models.validate_no_sepecial_characters]),
        ),
        migrations.AlterField(
            model_name='student',
            name='nume',
            field=models.TextField(validators=[curs_manager.models.validate_no_num_in_name, curs_manager.models.validate_no_sepecial_characters]),
        ),
        migrations.AlterField(
            model_name='student',
            name='prenume',
            field=models.TextField(validators=[curs_manager.models.validate_no_num_in_name, curs_manager.models.validate_no_sepecial_characters]),
        ),
    ]