# Generated by Django 5.0.4 on 2024-04-11 14:27

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("materials", "0002_alter_course_options_alter_lesson_options"),
    ]

    operations = [
        migrations.AlterField(
            model_name="lesson",
            name="course",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="lesson",
                to="materials.course",
                verbose_name="курс",
            ),
        ),
    ]
