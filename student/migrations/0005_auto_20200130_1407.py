# Generated by Django 3.0.2 on 2020-01-30 14:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0004_auto_20200130_1407'),
    ]

    operations = [
        migrations.AlterField(
            model_name='academicinfo',
            name='registration_no',
            field=models.IntegerField(default=389369, unique=True),
        ),
    ]
