# Generated by Django 2.0.1 on 2018-04-22 16:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0009_accountstatus'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='accountstatus',
            name='user_name',
        ),
    ]