# Generated by Django 3.2.4 on 2021-06-17 15:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mblog', '0003_profile'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='image',
            field=models.ImageField(default='default.jpg', upload_to='pics'),
        ),
    ]