# Generated by Django 2.2.4 on 2019-08-29 19:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='tb_Registration',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('technology', models.CharField(max_length=225)),
                ('trainer_name', models.CharField(max_length=225)),
                ('lab_assign', models.CharField(max_length=225)),
                ('batch_type', models.TextField(max_length=10)),
                ('batch_status', models.CharField(max_length=15)),
                ('batch_code', models.TextField(max_length=10)),
            ],
        ),
    ]
