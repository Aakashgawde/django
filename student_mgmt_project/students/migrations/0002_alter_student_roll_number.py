# Generated by Django 5.2.4 on 2025-07-05 14:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='roll_number',
            field=models.IntegerField(unique=True),
        ),
    ]
