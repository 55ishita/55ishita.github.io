# Generated by Django 3.1.7 on 2021-05-21 07:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0013_register_table_job'),
    ]

    operations = [
        migrations.RenameField(
            model_name='register_table',
            old_name='job',
            new_name='job_desc',
        ),
        migrations.AddField(
            model_name='register_table',
            name='job_email',
            field=models.CharField(blank=True, max_length=250),
        ),
        migrations.AddField(
            model_name='register_table',
            name='job_name',
            field=models.CharField(blank=True, max_length=250),
        ),
    ]
