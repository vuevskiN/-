# Generated by Django 5.0.6 on 2024-06-17 14:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='author_text',
            field=models.TextField(blank=True, null=True),
        ),
    ]
