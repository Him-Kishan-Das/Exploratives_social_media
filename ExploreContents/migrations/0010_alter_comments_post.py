# Generated by Django 5.0.4 on 2024-07-28 05:04

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ExploreContents', '0009_comments'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comments',
            name='post',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='post_comment', to='ExploreContents.post'),
        ),
    ]