# Generated by Django 5.0.4 on 2024-04-16 03:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("users", "0003_alter_payment_user"),
    ]

    operations = [
        migrations.AddField(
            model_name="user",
            name="role",
            field=models.CharField(
                choices=[("member", "member"), ("moderator", "moderator")],
                default="member",
                max_length=9,
            ),
        ),
    ]
