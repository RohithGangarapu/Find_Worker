# Generated by Django 4.2.16 on 2025-02-28 16:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('workers', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customer',
            name='address',
        ),
        migrations.AddField(
            model_name='customer',
            name='latitude',
            field=models.FloatField(default=0.0, max_length=255),
        ),
        migrations.AddField(
            model_name='customer',
            name='longitude',
            field=models.FloatField(default=0.0, max_length=255),
        ),
        migrations.AddField(
            model_name='customer',
            name='password',
            field=models.CharField(default='pass', max_length=255),
        ),
        migrations.AddField(
            model_name='worker',
            name='password',
            field=models.CharField(default='pass', max_length=255),
        ),
        migrations.AlterField(
            model_name='customer',
            name='user',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='worker',
            name='user',
            field=models.CharField(max_length=255),
        ),
    ]
