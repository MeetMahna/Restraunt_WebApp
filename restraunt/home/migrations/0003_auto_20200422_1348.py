# Generated by Django 3.0.5 on 2020-04-22 08:18

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('home', '0002_food_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='food',
            name='user',
        ),
        migrations.AddField(
            model_name='item',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='food', to=settings.AUTH_USER_MODEL),
        ),
    ]
