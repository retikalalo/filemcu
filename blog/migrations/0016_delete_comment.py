# Generated by Django 4.1.3 on 2022-12-13 07:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0015_rename_komen_comment'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Comment',
        ),
    ]
