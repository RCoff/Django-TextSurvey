# Generated by Django 3.2.6 on 2021-08-28 07:03

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('text_app', '0007_auto_20210828_0302'),
    ]

    operations = [
        migrations.AlterField(
            model_name='activesurveystore',
            name='active_survey_id',
            field=models.UUIDField(default=uuid.UUID('0cbc569f-7d41-4c54-aa91-8ff06fbd37d4'), primary_key=True, serialize=False),
        ),
    ]
