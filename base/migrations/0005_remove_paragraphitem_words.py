# Generated by Django 4.2 on 2023-04-20 17:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0004_alter_paragraphitem_words'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='paragraphitem',
            name='words',
        ),
    ]
