# Generated by Django 4.0 on 2021-12-18 10:28

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Video',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('publishing_date', models.DateTimeField()),
                ('thumbnail_url', models.URLField()),
            ],
        ),
    ]