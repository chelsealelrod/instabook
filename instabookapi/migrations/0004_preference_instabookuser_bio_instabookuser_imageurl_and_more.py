# Generated by Django 4.1 on 2022-09-17 20:28

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('instabookapi', '0003_alter_profile_location'),
    ]

    operations = [
        migrations.CreateModel(
            name='Preference',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', models.IntegerField()),
                ('date', models.DateTimeField(auto_now=True)),
                ('post', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='instabookapi.post', verbose_name='Post')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL, verbose_name='User')),
            ],
            options={
                'unique_together': {('user', 'post', 'value')},
            },
        ),
        migrations.AddField(
            model_name='instabookuser',
            name='bio',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='instabookuser',
            name='imageURL',
            field=models.ImageField(blank=True, upload_to='bio_image'),
        ),
        migrations.AddField(
            model_name='instabookuser',
            name='location',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.DeleteModel(
            name='Profile',
        ),
    ]
