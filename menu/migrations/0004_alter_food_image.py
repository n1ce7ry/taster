# Generated by Django 5.0 on 2024-01-13 14:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0003_alter_foodtype_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='food',
            name='image',
            field=models.ImageField(upload_to='menu/'),
        ),
    ]
