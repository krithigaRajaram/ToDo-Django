# Generated by Django 5.0 on 2023-12-29 06:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0002_list_user'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='list',
            options={'ordering': ['-updated', '-created']},
        ),
    ]