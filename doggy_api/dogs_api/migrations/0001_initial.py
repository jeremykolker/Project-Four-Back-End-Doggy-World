# Generated by Django 4.2 on 2023-04-16 16:01

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Dog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=32)),
                ('age', models.IntegerField()),
                ('breed', models.CharField(max_length=50)),
                ('walk_time', models.TimeField()),
                ('feeding_instructions', models.CharField(max_length=50)),
            ],
        ),
    ]