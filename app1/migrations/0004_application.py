# Generated by Django 4.0.3 on 2022-05-17 04:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0003_cemetery_burialplace_is_busy_burialplace_is_reserved_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Application',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('account', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app1.account')),
                ('burial_place', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='app1.burialplace')),
                ('deceased', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app1.deceased')),
            ],
        ),
    ]
