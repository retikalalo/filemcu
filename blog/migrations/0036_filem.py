# Generated by Django 4.1.3 on 2022-12-16 04:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0035_delete_filem'),
    ]

    operations = [
        migrations.CreateModel(
            name='Filem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=100, null=True)),
                ('poster_path', models.URLField(blank=True, null=True)),
                ('overview', models.TextField(blank=True, null=True)),
            ],
            options={
                'verbose_name_plural': 'Filem',
            },
        ),
    ]
