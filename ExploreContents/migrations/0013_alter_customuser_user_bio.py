# Generated by Django 5.0.4 on 2024-07-29 07:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ExploreContents', '0012_customuser_profile_picture_customuser_user_bio'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='user_bio',
            field=models.TextField(blank=True, null=True),
        ),
    ]