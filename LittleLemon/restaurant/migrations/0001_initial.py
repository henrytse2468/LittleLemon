# Generated by Django 5.0 on 2024-01-14 05:30

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Booking',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=200)),
                ('reservation_date', models.DateField()),
                ('reservation_slot', models.SmallIntegerField(default=10)),
            ],
        ),
        migrations.CreateModel(
            name='Menu',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('price', models.DecimalField(decimal_places=2, default=0, max_digits=10)),
                ('inventory', models.SmallIntegerField()),
                ('menu_item_description', models.TextField(default='', max_length=1000)),
            ],
        ),
    ]
