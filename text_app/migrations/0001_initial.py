# Generated by Django 3.2.6 on 2021-08-27 03:02

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ResponseModel',
            fields=[
                ('id', models.UUIDField(default=uuid.UUID('6cfa83be-5ed4-4f0d-91e2-55a02e0e2107'), primary_key=True, serialize=False)),
                ('mood_response', models.CharField(max_length=100)),
                ('datetime', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
