# Generated by Django 3.2.4 on 2021-06-26 12:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('college', '0003_auto_20210626_1214'),
    ]

    operations = [
        migrations.AlterField(
            model_name='branch',
            name='BRImg',
            field=models.ImageField(upload_to='static/img/branchs'),
        ),
    ]
