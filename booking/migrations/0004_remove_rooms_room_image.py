# Generated by Django 3.2.9 on 2022-03-02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0003_auto_20200304_1726'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='rooms',
            name='room_image',
        ),
    ]
