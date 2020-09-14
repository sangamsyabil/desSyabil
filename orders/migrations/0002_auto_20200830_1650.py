# Generated by Django 3.1 on 2020-08-30 16:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='status',
            field=models.CharField(choices=[('created', 'Created'), ('paid', 'Paid'), ('shipped', 'Shipped'), ('refund_requested', 'Refund Requested'), ('refunded', 'Refunded')], default='created', max_length=120),
        ),
    ]