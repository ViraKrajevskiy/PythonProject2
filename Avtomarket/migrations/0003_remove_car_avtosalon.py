# Generated by Django 5.1.6 on 2025-02-14 13:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Avtomarket', '0002_car'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='car',
            name='avtosalon',
        ),
    ]
