# Generated by Django 3.0.8 on 2020-07-28 07:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0011_roi_divided_area'),
    ]

    operations = [
        migrations.RenameField(
            model_name='roi_divided',
            old_name='Area',
            new_name='area',
        ),
    ]