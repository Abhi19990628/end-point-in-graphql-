# Generated by Django 5.0.7 on 2024-07-25 13:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='author',
            name='age',
        ),
        migrations.RemoveField(
            model_name='post',
            name='context',
        ),
        migrations.AddField(
            model_name='post',
            name='content',
            field=models.TextField(default=1),
            preserve_default=False,
        ),
    ]
