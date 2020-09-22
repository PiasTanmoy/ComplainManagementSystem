# Generated by Django 3.0.3 on 2020-09-22 08:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Complain', '0006_auto_20200922_1419'),
    ]

    operations = [
        migrations.AlterField(
            model_name='complain',
            name='status',
            field=models.CharField(choices=[('Approved', 'Approved'), ('Not Approved', 'Not Approved'), ('Not Approved', 'Pending')], default='Approved', max_length=100),
        ),
        migrations.AlterField(
            model_name='complain',
            name='type',
            field=models.CharField(choices=[('General', 'General'), ('Departmental', 'Departmental'), ('Both', 'Both')], default='General', max_length=100),
        ),
    ]