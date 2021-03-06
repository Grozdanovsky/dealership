# Generated by Django 4.0.1 on 2022-02-20 14:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('dealership', '0003_userservice'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserServiceVehicle',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('placed_at', models.DateTimeField(auto_now_add=True)),
                ('payment_status', models.CharField(choices=[('P', 'Pending'), ('C', 'Complete'), ('F', 'Failed')], default='P', max_length=1)),
                ('service_status', models.CharField(choices=[('F', 'Finished'), ('X', 'Unfinished')], default='X', max_length=1)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dealership.user')),
            ],
        ),
        migrations.RemoveField(
            model_name='userservice',
            name='service',
        ),
        migrations.RemoveField(
            model_name='userservice',
            name='user',
        ),
        migrations.AddField(
            model_name='vehicle',
            name='service',
            field=models.PositiveIntegerField(default=1000),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='vehicle',
            name='cubic_meters',
            field=models.PositiveIntegerField(),
        ),
        migrations.AlterField(
            model_name='vehicle',
            name='horsepower',
            field=models.PositiveIntegerField(),
        ),
        migrations.DeleteModel(
            name='Service',
        ),
        migrations.DeleteModel(
            name='UserService',
        ),
        migrations.AddField(
            model_name='userservicevehicle',
            name='vehicle',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dealership.vehicle'),
        ),
    ]
