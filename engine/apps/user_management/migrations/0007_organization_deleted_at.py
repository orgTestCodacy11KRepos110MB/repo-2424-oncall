# Generated by Django 3.2.16 on 2023-01-04 05:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_management', '0006_organization_uuid'),
    ]

    operations = [
        migrations.AddField(
            model_name='organization',
            name='deleted_at',
            field=models.DateTimeField(null=True),
        ),
    ]
