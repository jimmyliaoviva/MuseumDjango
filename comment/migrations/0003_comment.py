# Generated by Django 3.0.3 on 2020-11-27 15:59

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('main', '0005_delete_comment'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('comment', '0002_delete_comment'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('commentid', models.AutoField(primary_key=True, serialize=False)),
                ('comment', models.CharField(max_length=1500)),
                ('commenttime', models.DateTimeField(auto_now=True)),
                ('museum', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.Museum')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
