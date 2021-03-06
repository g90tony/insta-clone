# Generated by Django 3.2.3 on 2021-05-26 12:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('image', '0003_auto_20210526_1512'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comment',
            old_name='image_id',
            new_name='image',
        ),
        migrations.AddField(
            model_name='comment',
            name='profile',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='image.profile'),
            preserve_default=False,
        ),
    ]
