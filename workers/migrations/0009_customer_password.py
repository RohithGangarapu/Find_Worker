# Generated by Django 4.2.16 on 2025-03-01 22:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('workers', '0008_worker_password'),
    ]

    operations = [
        migrations.AddField(
            model_name='customer',
            name='password',
            field=models.CharField(default='None', max_length=50),
        ),
    ]
