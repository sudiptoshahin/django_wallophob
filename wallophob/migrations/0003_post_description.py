# Generated by Django 2.1.5 on 2022-03-27 19:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wallophob', '0002_auto_20220327_0005'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='description',
            field=models.TextField(null=True),
        ),
    ]
