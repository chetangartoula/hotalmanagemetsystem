# Generated by Django 4.0.5 on 2022-06-30 13:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restaurant', '0002_remove_user_groups_remove_user_user_permissions_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='user',
            field=models.CharField(max_length=255),
        ),
    ]