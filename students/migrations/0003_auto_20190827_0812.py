# Generated by Django 2.2.4 on 2019-08-27 13:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0002_auto_20190827_0756'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='student_photo',
            field=models.ImageField(upload_to='images/'),
        ),
    ]