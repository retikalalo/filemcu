# Generated by Django 4.1.3 on 2022-12-09 08:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_rename_api_key_api_key'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='api',
            name='key',
        ),
        migrations.AddField(
            model_name='api',
            name='description',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='api',
            name='image',
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='api',
            name='title',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
