# Generated by Django 4.1a1 on 2023-07-06 12:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('person', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='name',
            field=models.TextField(max_length=50),
        ),
    ]