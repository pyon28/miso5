# Generated by Django 4.1 on 2024-01-31 08:41

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_remove_items_appearance_rating_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='items',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
