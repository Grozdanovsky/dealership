# Generated by Django 4.0.1 on 2022-02-16 17:41

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company_name', models.CharField(max_length=255)),
                ('CEO', models.CharField(max_length=255)),
                ('revenue', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Type',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Vehicle',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False)),
                ('manufacturer', models.CharField(max_length=255)),
                ('model', models.CharField(max_length=255)),
                ('horsepower', models.IntegerField()),
                ('cubic_meters', models.IntegerField()),
                ('color', models.CharField(max_length=255)),
                ('year', models.IntegerField()),
                ('price', models.PositiveBigIntegerField()),
                ('quantity', models.PositiveIntegerField()),
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dealership.company')),
                ('type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dealership.type')),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=255)),
                ('last_name', models.CharField(max_length=255)),
                ('email', models.EmailField(max_length=254)),
                ('vehicle', models.ManyToManyField(blank=True, to='dealership.Vehicle')),
            ],
        ),
    ]
