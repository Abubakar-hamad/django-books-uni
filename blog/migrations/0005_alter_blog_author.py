# Generated by Django 3.2.4 on 2021-06-28 16:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_alter_blog_contents'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='author',
            field=models.CharField(default='admin', max_length=100),
        ),
    ]