# Generated by Django 3.1.3 on 2020-11-30 17:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('asn', '0015_auto_20201129_1444'),
    ]

    operations = [
        migrations.AddField(
            model_name='asndetailmodel',
            name='goods_more_qty',
            field=models.IntegerField(default=0, verbose_name='Goods More QTY'),
        ),
    ]
