# Generated by Django 4.1a1 on 2023-07-06 12:01

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('salary', models.FloatField()),
                ('post', models.CharField(max_length=100)),
                ('cover', models.ImageField(blank=True, upload_to='covers/')),
            ],
        ),
    ]
