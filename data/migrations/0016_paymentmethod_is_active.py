# Generated by Django 4.1.5 on 2023-01-18 21:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('data', '0015_paymentmethod_api_key_conf'),
    ]

    operations = [
        migrations.AddField(
            model_name='paymentmethod',
            name='is_active',
            field=models.BooleanField(default=True),
        ),
    ]