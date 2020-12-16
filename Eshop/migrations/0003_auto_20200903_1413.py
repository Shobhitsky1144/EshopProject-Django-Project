# Generated by Django 3.0.6 on 2020-09-03 08:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Eshop', '0002_auto_20200903_1114'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cat_name', models.CharField(max_length=100)),
                ('cover_pic', models.FileField(upload_to='categories/%y/%m/%d')),
                ('description', models.TextField()),
                ('added_on', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.AlterModelOptions(
            name='contact_us',
            options={'verbose_name_plural': 'Contact'},
        ),
        migrations.AlterModelOptions(
            name='student',
            options={'verbose_name_plural': 'Student'},
        ),
    ]
