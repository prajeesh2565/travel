# Generated by Django 4.2.2 on 2023-07-06 05:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('travelapk', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='team',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=35)),
                ('img', models.ImageField(upload_to='pics')),
                ('info', models.TextField()),
            ],
        ),
    ]
