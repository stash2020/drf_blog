# Generated by Django 4.0.4 on 2022-04-15 10:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0012_remove_like_status'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='like',
            name='like_id',
        ),
    ]
