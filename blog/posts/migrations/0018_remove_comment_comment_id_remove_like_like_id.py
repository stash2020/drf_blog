# Generated by Django 4.0.4 on 2022-04-16 12:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0017_alter_comment_comment_id_alter_like_like_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='comment_id',
        ),
        migrations.RemoveField(
            model_name='like',
            name='like_id',
        ),
    ]