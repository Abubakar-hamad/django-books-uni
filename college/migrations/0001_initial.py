# Generated by Django 3.2.4 on 2021-06-24 15:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Branch',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('BRImg', models.ImageField(upload_to='')),
                ('BRdescrip', models.TextField(max_length=1000)),
            ],
        ),
        migrations.CreateModel(
            name='College',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('CLtitle', models.CharField(max_length=200)),
                ('CLdescrip', models.TextField(max_length=1000)),
                ('CLdepart', models.CharField(choices=[('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5'), ('6', '6'), ('7', '7')], max_length=200, verbose_name='Department_Number')),
            ],
        ),
        migrations.CreateModel(
            name='Department',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Dtitle', models.CharField(max_length=200, verbose_name='Department_name')),
                ('Dsystem', models.CharField(choices=[('نظام سنوي', ' نظام سنوي'), ('نظام الفصول', 'نظام الفصول')], max_length=200, verbose_name='study_system')),
                ('Dcollege', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='college.college', verbose_name='College')),
            ],
        ),
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Btitle', models.CharField(max_length=200, verbose_name='Book name')),
                ('Bclass', models.CharField(choices=[('First', 'First'), ('Second ', 'Second '), ('Third', 'Third'), ('Fourth', 'Forth'), ('Fifth', 'Fifth'), ('Sixth', 'Sixth'), ('seventh', 'seventh'), ('Eighth', 'Eighth'), ('ninth', 'ninth'), ('tenth', 'tenth')], max_length=20, verbose_name='Semester')),
                ('Bdescrip', models.TextField(max_length=1000, verbose_name='Desciption')),
                ('Bcollge', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='college.college', verbose_name='College')),
                ('Bdepart', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='college.department', verbose_name='Department')),
            ],
        ),
    ]
