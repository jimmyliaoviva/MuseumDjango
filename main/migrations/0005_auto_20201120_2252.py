# Generated by Django 3.1.2 on 2020-11-20 14:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_auto_20201120_2214'),
    ]

    operations = [
        migrations.AlterField(
            model_name='museum',
            name='address',
            field=models.CharField(blank=True, max_length=100, unique=True),
        ),
        migrations.AlterField(
            model_name='museum',
            name='img',
            field=models.CharField(blank=True, default=None, max_length=1500),
        ),
        migrations.AlterField(
            model_name='museum',
            name='introduce',
            field=models.CharField(blank=True, default=None, max_length=1500),
        ),
        migrations.AlterField(
            model_name='museum',
            name='latitude',
            field=models.FloatField(blank=True, default=None),
        ),
        migrations.AlterField(
            model_name='museum',
            name='longitude',
            field=models.FloatField(blank=True, default=None),
        ),
        migrations.AlterField(
            model_name='museum',
            name='website',
            field=models.URLField(blank=True, default=None, max_length=500),
        ),
    ]
