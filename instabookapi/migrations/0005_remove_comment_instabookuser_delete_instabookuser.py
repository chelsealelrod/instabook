# Generated by Django 4.1 on 2022-09-22 00:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('instabookapi', '0004_preference_instabookuser_bio_instabookuser_imageurl_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='instabookuser',
        ),
        migrations.DeleteModel(
            name='InstaBookUser',
        ),
    ]