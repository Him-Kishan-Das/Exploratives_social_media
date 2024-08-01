# Generated by Django 5.0.4 on 2024-08-01 08:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ExploreContents', '0013_alter_customuser_user_bio'),
    ]

    operations = [
        migrations.AddField(
            model_name='follow',
            name='is_active',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='profile_picture',
            field=models.ImageField(blank=True, default='static/profilePic/default.png', null=True, upload_to='profilePic'),
        ),
    ]
