# Generated by Django 3.0.3 on 2020-09-21 19:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Student', '0004_auto_20200922_0100'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='email',
            field=models.EmailField(max_length=254, unique=True),
        ),
    ]
