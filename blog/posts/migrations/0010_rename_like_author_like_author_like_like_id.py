# Generated by Django 4.0.4 on 2022-04-15 09:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0009_rename_like_post_like_parent'),
    ]

    operations = [
        migrations.RenameField(
            model_name='like',
            old_name='like_author',
            new_name='author',
        ),
        migrations.AddField(
            model_name='like',
            name='like_id',
            field=models.IntegerField(default=1),
        ),
    ]
