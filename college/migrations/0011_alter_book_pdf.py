# Generated by Django 3.2.5 on 2021-07-02 22:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('college', '0010_auto_20210701_1904'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='pdf',
            field=models.FileField(blank=True, null=True, upload_to='static/pdf/Books'),
        ),
    ]
