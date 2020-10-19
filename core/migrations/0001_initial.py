# Generated by Django 3.1.2 on 2020-10-19 11:21

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Pet',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('city', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('phone', models.CharField(max_length=11)),
                ('email', models.EmailField(max_length=254)),
                ('begin_date', models.DateTimeField(auto_now_add=True)),
                ('photo', models.ImageField(upload_to='')),
                ('active', models.BooleanField(default=True)),
            ],
        ),
    ]
