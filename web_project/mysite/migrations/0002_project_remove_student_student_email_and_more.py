# Generated by Django 5.0.6 on 2024-07-05 05:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mysite', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('topic', models.CharField(max_length=100)),
                ('duration', models.IntegerField()),
                ('languages', models.CharField(max_length=100)),
            ],
        ),
        migrations.RemoveField(
            model_name='student',
            name='student_email',
        ),
        migrations.RemoveField(
            model_name='student',
            name='student_name',
        ),
        migrations.RemoveField(
            model_name='student',
            name='student_phone',
        ),
        migrations.RemoveField(
            model_name='student',
            name='student_sem',
        ),
        migrations.RemoveField(
            model_name='student',
            name='student_usn',
        ),
        migrations.AddField(
            model_name='student',
            name='name',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AddField(
            model_name='student',
            name='usn',
            field=models.CharField(default='', max_length=10),
        ),
        migrations.AddField(
            model_name='student',
            name='projects',
            field=models.ManyToManyField(to='mysite.project'),
        ),
        migrations.DeleteModel(
            name='Course',
        ),
    ]
