# Generated by Django 5.0.6 on 2024-11-11 13:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('notes', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='subject',
            name='sub_icon',
            field=models.ImageField(blank=True, null=True, upload_to='icons/'),
        ),
    ]
