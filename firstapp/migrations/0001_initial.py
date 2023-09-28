# Generated by Django 4.2.5 on 2023-09-27 10:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255)),
                ('cost', models.DecimalField(decimal_places=2, max_digits=10)),
                ('quantity', models.PositiveIntegerField()),
                ('quantity_sold', models.PositiveIntegerField()),
                ('selling_price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('profit_earned', models.DecimalField(decimal_places=2, max_digits=10)),
                ('revenue', models.DecimalField(decimal_places=2, max_digits=10)),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255)),
                ('quantity', models.PositiveBigIntegerField(default=0)),
                ('cost', models.DecimalField(decimal_places=2, max_digits=10)),
                ('orderdttm', models.DateTimeField()),
                ('is_received', models.BooleanField(default=False)),
                ('is_cancel', models.BooleanField(default=False)),
                ('item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='firstapp.item')),
            ],
        ),
    ]
