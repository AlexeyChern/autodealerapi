# Generated by Django 3.1.7 on 2021-03-18 11:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('JobTestAPI', '0002_auto_20210318_1129'),
    ]

    operations = [
        migrations.AddField(
            model_name='cars',
            name='BrandName',
            field=models.CharField(default='Unknown brand', max_length=50),
        ),
        migrations.AlterField(
            model_name='cars',
            name='ModelName',
            field=models.CharField(default='Unknown model', max_length=50),
        ),
        migrations.AlterField(
            model_name='dealer',
            name='CompanyName',
            field=models.CharField(default='Unknown company', max_length=50),
        ),
    ]
