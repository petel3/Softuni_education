# Generated by Django 4.0.2 on 2022-02-11 16:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0003_alter_pet_unique_together_petphoto'),
    ]

    operations = [
        migrations.AlterField(
            model_name='petphoto',
            name='photo',
            field=models.ImageField(upload_to=''),
        ),
    ]