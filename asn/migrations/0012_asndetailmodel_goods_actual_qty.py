# Generated by Django 3.1.3 on 2020-11-26 22:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('asn', '0011_auto_20201126_2258'),
    ]

    operations = [
        migrations.AddField(
            model_name='asndetailmodel',
            name='goods_actual_qty',
            field=models.IntegerField(default=0, verbose_name='Goods Actual QTY'),
        ),
    ]
