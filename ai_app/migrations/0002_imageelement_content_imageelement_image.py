# Generated by Django 5.0.2 on 2024-03-02 10:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ai_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='imageelement',
            name='content',
            field=models.TextField(default=''),
        ),
        migrations.AddField(
            model_name='imageelement',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='media'),
        ),
    ]
