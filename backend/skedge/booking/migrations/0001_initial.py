# Generated by Django 3.1 on 2020-08-06 04:00

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Business',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('business_name', models.CharField(max_length=50)),
                ('short_description', models.CharField(max_length=200)),
                ('long_description', models.CharField(max_length=3000)),
                ('contact_email', models.CharField(max_length=50)),
                ('phone_number', models.CharField(max_length=14)),
                ('category', models.CharField(choices=[('fitness', 'Fitness'), ('wellness', 'Wellness'), ('beauty', 'Beauty')], max_length=50)),
                ('address', models.CharField(max_length=200)),
                ('city', models.CharField(max_length=100)),
                ('state', models.CharField(max_length=100)),
                ('postal_code', models.CharField(max_length=6)),
                ('country', models.CharField(max_length=100)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone_number', models.CharField(default='', max_length=14)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.CharField(max_length=200)),
                ('price', models.DecimalField(decimal_places=2, max_digits=8)),
                ('duration', models.IntegerField(choices=[(15, 'Quarter hour'), (30, 'Half hour'), (45, 'Three quarters hour'), (60, 'One hour'), (90, 'One and a half hours'), (120, 'Two hours'), (150, 'Two and a half hours'), (180, 'Three hours')])),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('business', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='booking.business')),
            ],
        ),
        migrations.CreateModel(
            name='Favorites',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('business', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='booking.business')),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='booking.customer')),
            ],
        ),
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=254)),
                ('business', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='booking.business')),
            ],
        ),
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('business', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='booking.business')),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='booking.customer')),
            ],
        ),
        migrations.CreateModel(
            name='Appointment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_time', models.DateTimeField()),
                ('end_time', models.DateTimeField()),
                ('cancelled', models.BooleanField(default=False)),
                ('cancelled_by_customer', models.BooleanField(default=False)),
                ('cancelled_by_business', models.BooleanField(default=False)),
                ('business', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='booking.business')),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='booking.customer')),
                ('service', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='booking.service')),
            ],
        ),
    ]
