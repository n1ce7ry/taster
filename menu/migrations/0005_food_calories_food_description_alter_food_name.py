# Generated by Django 5.0 on 2024-01-17 14:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0004_alter_food_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='food',
            name='calories',
            field=models.IntegerField(default=500),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='food',
            name='description',
            field=models.CharField(default='test', max_length=255),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='food',
            name='name',
            field=models.CharField(max_length=80),
        ),
    ]
