# Generated by Django 3.0.2 on 2020-01-20 16:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_auto_20200120_1526'),
    ]

    operations = [
        migrations.AlterField(
            model_name='main',
            name='fb',
            field=models.CharField(default='-', max_length=30),
        ),
        migrations.AlterField(
            model_name='main',
            name='name',
            field=models.CharField(max_length=30),
        ),
        migrations.AlterField(
            model_name='main',
            name='tw',
            field=models.CharField(default='-', max_length=30),
        ),
        migrations.AlterField(
            model_name='main',
            name='yt',
            field=models.CharField(default='-', max_length=30),
        ),
    ]
