# Generated by Django 3.0.6 on 2020-09-07 06:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Eshop', '0004_auto_20200904_0030'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='gender',
            field=models.CharField(choices=[('F', 'Female'), ('M', 'Male')], max_length=150),
        ),
    ]
