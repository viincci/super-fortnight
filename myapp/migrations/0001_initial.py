# Generated by Django 4.0.3 on 2022-04-08 14:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Categories',
            fields=[
                ('cat_id', models.IntegerField(primary_key=True, serialize=False, unique=True)),
                ('name', models.CharField(max_length=50)),
                ('description', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Reference',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=70)),
                ('occupation', models.TextField(max_length=1024)),
                ('Qoute', models.TextField(max_length=1024)),
            ],
        ),
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=70)),
                ('description', models.TextField(max_length=1024)),
                ('Image', models.ImageField(upload_to='media', verbose_name='')),
                ('thumb', models.ImageField(upload_to='media', verbose_name='')),
            ],
        ),
        migrations.CreateModel(
            name='Award',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=70)),
                ('description', models.TextField(blank=True, max_length=1024, null=True)),
                ('Image', models.ImageField(upload_to='media', verbose_name='')),
                ('Year', models.IntegerField()),
                ('Position', models.CharField(max_length=50)),
                ('category', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='myapp.categories')),
            ],
        ),
    ]
