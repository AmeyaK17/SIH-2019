# Generated by Django 2.1.7 on 2019-03-02 16:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('doctors', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='case',
            name='Docs',
        ),
    ]
