# Generated by Django 4.1.5 on 2023-01-24 19:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('data', '0036_tguser_chat_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='payment',
            name='fiat_amount',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
    ]