# Generated by Django 2.2.13 on 2020-06-07 17:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_comment'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comment',
            old_name='author',
            new_name='commentAuthor',
        ),
    ]
