# Generated by Django 4.0.1 on 2022-02-18 18:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('dealership', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='company',
            options={'ordering': ['id']},
        ),
        migrations.AlterModelOptions(
            name='vehicle',
            options={'ordering': ['company']},
        ),
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('service_cost', models.IntegerField()),
                ('vehicle', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='dealership.vehicle')),
            ],
        ),
    ]
