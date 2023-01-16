# Generated by Django 4.1.5 on 2023-01-16 14:10

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('data', '0008_alter_currencydetail_code_giftorder'),
    ]

    operations = [
        migrations.AddField(
            model_name='giftorder',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='giftorder',
            name='amount',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='giftorder',
            name='status',
            field=models.CharField(choices=[('Open', 'open'), ('Pending', 'pending'), ('Payment Received', 'peyment received'), ('Complete', 'complete')], max_length=128),
        ),
    ]
