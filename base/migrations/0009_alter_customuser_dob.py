# Generated by Django 4.2 on 2023-04-21 11:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0008_delete_paragraphsgroup'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='dob',
            field=models.CharField(blank=True, max_length=10),
        ),
    ]