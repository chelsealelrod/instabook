# Generated by Django 4.1 on 2022-09-12 23:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('instabookapi', '0002_remove_comment_user_remove_post_user_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='location',
            field=models.CharField(blank=True, max_length=100),
        ),
    ]