# Generated by Django 4.1.2 on 2022-11-18 10:36

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('photos', '0004_alter_photo_photo'),
    ]

    operations = [
        migrations.AddField(
            model_name='photo',
            name='user',
            field=models.ForeignKey(default='1', on_delete=django.db.models.deletion.RESTRICT, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
    ]
