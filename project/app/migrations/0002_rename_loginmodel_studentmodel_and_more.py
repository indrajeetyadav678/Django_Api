# Generated by Django 5.0.4 on 2024-04-12 06:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Loginmodel',
            new_name='StudentModel',
        ),
        migrations.AlterModelOptions(
            name='studentmodel',
            options={'verbose_name': 'Student', 'verbose_name_plural': 'Student'},
        ),
    ]
