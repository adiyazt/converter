# Generated by Django 5.0.1 on 2024-04-15 14:52

import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='WordFile',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False)),
                ('filename', models.CharField(max_length=32)),
            ],
        ),
    ]
