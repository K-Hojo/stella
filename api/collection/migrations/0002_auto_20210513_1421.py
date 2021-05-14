# Generated by Django 3.1.7 on 2021-05-13 05:21

import collection.models
import django.contrib.postgres.fields
from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('collection', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='collection',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='collection',
            name='updated_at',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='collection',
            name='books',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.JSONField(blank=True, default=collection.models.book_json_default_value), size=None),
        ),
    ]