# Generated by Django 3.0.3 on 2020-09-21 19:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Student', '0003_auto_20200920_1832'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='email',
            field=models.EmailField(blank=True, max_length=254, unique=True),
        ),
    ]
