# Generated by Django 4.1a1 on 2023-05-11 09:00

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Table',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.TextField()),
                ('view', models.TextField()),
                ('live', models.IntegerField()),
                ('age', models.IntegerField()),
            ],
        ),
    ]
