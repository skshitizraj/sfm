# Generated by Django 3.0.8 on 2020-07-28 07:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0010_auto_20200728_0603'),
    ]

    operations = [
        migrations.AddField(
            model_name='roi_divided',
            name='Area',
            field=models.FloatField(max_length=100, null=True),
        ),
    ]
