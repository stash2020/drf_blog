# Generated by Django 4.0.4 on 2022-04-16 10:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0016_like_like_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='comment_id',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='like',
            name='like_id',
            field=models.IntegerField(),
        ),
    ]
