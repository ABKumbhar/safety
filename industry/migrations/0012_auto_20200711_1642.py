# Generated by Django 3.0.6 on 2020-07-11 11:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('industry', '0011_equipment_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='industry',
            name='slug',
            field=models.SlugField(blank=True, default='a', null=True),
        ),
    ]