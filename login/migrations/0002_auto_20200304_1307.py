# Generated by Django 3.2.9 on 2022-03-02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='phone_no',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='customer',
            name='profile_pic',
            field=models.ImageField(blank=True, upload_to='media'),
        ),
        migrations.AlterField(
            model_name='roommanager',
            name='phone_no',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='roommanager',
            name='profile_pic',
            field=models.ImageField(blank=True, upload_to='media'),
        ),
    ]
