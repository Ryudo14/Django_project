# Generated by Django 4.1a1 on 2023-05-19 07:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_comment'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comment',
            old_name='article',
            new_name='title',
        ),
    ]
