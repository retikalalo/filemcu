# Generated by Django 4.1.3 on 2022-12-09 23:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0007_remove_api_key_api_description_api_image_and_more'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='API',
            new_name='Filem',
        ),
        migrations.AlterModelOptions(
            name='filem',
            options={'verbose_name_plural': 'Filem'},
        ),
    ]