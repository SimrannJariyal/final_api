# Generated by Django 5.0.6 on 2024-11-10 17:38

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Subject',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True)),
                ('description', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Unit',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('unit_name', models.CharField(max_length=100)),
                ('pdf_file', models.FileField(upload_to='pdfs/')),
                ('subject', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='units', to='notes.subject')),
            ],
        ),
    ]