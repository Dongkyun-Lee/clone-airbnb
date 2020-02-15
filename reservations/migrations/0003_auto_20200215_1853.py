# Generated by Django 2.2.5 on 2020-02-15 09:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reservations', '0002_auto_20200215_1844'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reservation',
            name='status',
            field=models.CharField(choices=[('confirmed', 'Confirmed'), ('canceled', 'Canceled'), ('pending', 'Pending')], default='pending', max_length=12),
        ),
    ]
