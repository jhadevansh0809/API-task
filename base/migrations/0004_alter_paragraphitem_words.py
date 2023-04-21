# Generated by Django 4.2 on 2023-04-20 17:05

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0003_alter_paragraphitem_words'),
    ]

    operations = [
        migrations.AlterField(
            model_name='paragraphitem',
            name='words',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=50), blank=True, size=1000),
        ),
    ]
