# Generated by Django 3.1.3 on 2020-11-24 20:15

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ListModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('api_name', models.CharField(max_length=32, verbose_name='接口名称')),
                ('api_describe', models.TextField(max_length=255, verbose_name='接口描述')),
                ('api_manager', models.CharField(max_length=11, verbose_name='接口负责人')),
                ('openid', models.CharField(max_length=255, verbose_name='Openid')),
                ('is_delete', models.BooleanField(default=False, verbose_name='Delete Label')),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='Create Time')),
                ('update_time', models.DateTimeField(auto_now=True, null=True, verbose_name='Update Time')),
            ],
            options={
                'verbose_name': 'data id',
                'verbose_name_plural': 'data id',
                'db_table': 'outbound',
                'ordering': ['-id'],
            },
        ),
    ]
