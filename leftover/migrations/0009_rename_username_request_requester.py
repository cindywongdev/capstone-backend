# Generated by Django 4.1.7 on 2023-03-10 00:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('leftover', '0008_alter_listing_restaurant'),
    ]

    operations = [
        migrations.RenameField(
            model_name='request',
            old_name='username',
            new_name='requester',
        ),
    ]