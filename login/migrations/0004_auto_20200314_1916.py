# Generated by Django 3.2.9 on 2022-03-02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0003_auto_20200314_1916'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='pin_code',
            field=models.IntegerField(blank=True),
        ),
    ]
