# Generated by Django 4.0.4 on 2022-05-27 10:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='technology',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='project',
            name='theme',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
    ]
