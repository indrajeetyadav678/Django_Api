# Generated by Django 5.0.4 on 2024-04-11 10:05

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Loginmodel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=200)),
                ('Userid', models.EmailField(max_length=254)),
                ('Number', models.IntegerField()),
                ('Password', models.CharField(max_length=200)),
                ('Con_password', models.CharField(max_length=200)),
            ],
            options={
                'verbose_name': 'Login',
                'verbose_name_plural': 'Login',
                'db_table': 'LoginData',
            },
        ),
    ]