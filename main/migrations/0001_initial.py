# Generated by Django 3.1.2 on 2020-11-13 07:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='City',
            fields=[
                ('cid', models.AutoField(primary_key=True, serialize=False)),
                ('cname', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Nation',
            fields=[
                ('nid', models.AutoField(primary_key=True, serialize=False)),
                ('nname', models.CharField(max_length=20, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Museum',
            fields=[
                ('cid', models.AutoField(primary_key=True, serialize=False)),
                ('mname', models.CharField(max_length=50, unique=True)),
                ('address', models.CharField(max_length=100, unique=True)),
                ('introduce', models.CharField(max_length=1500)),
                ('img', models.ImageField(upload_to='')),
                ('city', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.city')),
                ('nation', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.nation')),
            ],
        ),
        migrations.AddField(
            model_name='city',
            name='nation',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.nation'),
        ),
    ]
