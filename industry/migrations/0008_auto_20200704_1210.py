# Generated by Django 3.0.6 on 2020-07-04 06:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('industry', '0007_industry_trending'),
    ]

    operations = [
        migrations.AlterField(
            model_name='industry',
            name='name',
            field=models.CharField(max_length=100),
        ),
    ]