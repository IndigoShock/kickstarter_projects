# Generated by Django 2.1.1 on 2018-09-25 00:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('project_data', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='project',
            old_name='project_id',
            new_name='ID',
        ),
    ]
