# Generated by Django 4.1.3 on 2022-12-15 00:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0030_comment'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comment',
            old_name='body',
            new_name='komen',
        ),
    ]
