# Generated by Django 4.1.3 on 2022-12-14 12:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0026_alter_artikel_img'),
    ]

    operations = [
        migrations.AlterField(
            model_name='artikel',
            name='img',
            field=models.ImageField(blank=True, null=True, upload_to='img'),
        ),
    ]