# Generated by Django 5.0.4 on 2024-04-27 03:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("users", "0006_payment_link_payment_sessions_id_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="payment",
            name="payment_type",
            field=models.CharField(
                blank=True,
                choices=[("cash", "наличные"), ("spending", "перевод на счет")],
                max_length=32,
                null=True,
                verbose_name="способ оплаты",
            ),
        ),
    ]