# Generated by Django 4.0.5 on 2022-07-06 17:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0012_alter_shopitems_quantity_alter_shopitems_total'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shop',
            name='total',
            field=models.IntegerField(),
        ),
    ]