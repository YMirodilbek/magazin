# Generated by Django 4.0.5 on 2022-07-07 15:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0014_alter_shop_client_alter_shopitems_product_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='shopitems',
            name='total',
        ),
        migrations.AddField(
            model_name='shopitems',
            name='totalPay',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='shop',
            name='total',
            field=models.IntegerField(default=0),
        ),
    ]