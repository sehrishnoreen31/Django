# Generated by Django 5.2 on 2025-05-18 09:32

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('empno', models.CharField(max_length=50)),
                ('empname', models.CharField(max_length=50)),
                ('contact', models.CharField(max_length=50)),
                ('salary', models.IntegerField()),
                ('joined_date', models.DateField(auto_now=True)),
            ],
            options={
                'db_table': 'emplyee',
            },
        ),
    ]
