# Generated by Django 5.0.2 on 2024-03-09 13:42

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('payment', '0002_payments_cartorder_serviceorder'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Wallet',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('balance', models.IntegerField(default=0)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='WalletHistory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(blank=True, max_length=20, null=True)),
                ('created_at', models.DateField(auto_now_add=True)),
                ('amount', models.IntegerField()),
                ('reason', models.CharField(blank=True, max_length=255, null=True)),
                ('wallet', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='payment.wallet')),
            ],
        ),
    ]
