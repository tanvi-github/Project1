# Generated by Django 2.2.4 on 2019-09-04 06:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0002_tb_registration'),
    ]

    operations = [
        migrations.CreateModel(
            name='tb_TrainerRegistration',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=200)),
                ('Gender', models.CharField(max_length=200)),
                ('Employee_ID', models.CharField(max_length=200)),
                ('Email_ID', models.CharField(max_length=200)),
                ('Contact', models.CharField(max_length=200)),
                ('Password', models.CharField(max_length=200)),
            ],
        ),
        migrations.AlterField(
            model_name='tb_registration',
            name='batch_code',
            field=models.CharField(max_length=10),
        ),
        migrations.AlterField(
            model_name='tb_registration',
            name='batch_type',
            field=models.CharField(max_length=10),
        ),
    ]