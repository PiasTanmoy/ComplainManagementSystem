# Generated by Django 3.0.3 on 2020-09-23 15:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Student', '0005_auto_20200922_0106'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='user_name',
            field=models.CharField(max_length=100, unique=True),
        ),
    ]
