# Generated by Django 2.1.5 on 2019-02-05 05:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('item', '0002_auto_20190205_1402'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='price',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='item',
            name='btcpay_item_name',
            field=models.CharField(max_length=200),
        ),
    ]
