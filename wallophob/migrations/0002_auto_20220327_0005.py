# Generated by Django 2.1.5 on 2022-03-26 18:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wallophob', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='content',
        ),
        migrations.AddField(
            model_name='post',
            name='photo',
            field=models.FileField(null=True, upload_to=''),
        ),
    ]