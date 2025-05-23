# Generated by Django 5.2 on 2025-05-04 15:55

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=100)),
                ('image', models.ImageField(upload_to='blogs/')),
                ('paragraph', models.TextField(max_length=10000)),
                ('date', models.DateField(auto_now=True)),
            ],
        ),
    ]
