# Generated by Django 4.0.2 on 2022-02-23 19:01

import Expenses_Tracker.tracker_app.validators
import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=15, validators=[django.core.validators.MinLengthValidator(2), Expenses_Tracker.tracker_app.validators.only_letters_validator])),
                ('last_name', models.CharField(max_length=15, validators=[django.core.validators.MinLengthValidator(2), Expenses_Tracker.tracker_app.validators.only_letters_validator])),
                ('budget', models.FloatField(default=0, validators=[django.core.validators.MinValueValidator(0)])),
                ('profile_image', models.ImageField(blank=True, null=True, upload_to='profiles/', validators=[Expenses_Tracker.tracker_app.validators.MaxFileSizeValidator(5)])),
            ],
        ),
    ]
