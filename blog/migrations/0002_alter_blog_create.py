# Generated by Django 3.2.4 on 2021-06-27 00:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='create',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Created At'),
        ),
    ]
