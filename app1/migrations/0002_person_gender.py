# Generated by Django 4.0.3 on 2022-05-16 23:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='person',
            name='gender',
            field=models.CharField(blank=True, max_length=1, null=True),
        ),
    ]