# Generated by Django 3.2.4 on 2021-06-29 00:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('college', '0007_alter_book_pdf'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='pdf',
            field=models.FileField(blank=True, null=True, upload_to='static/pdf/Books'),
        ),
    ]
