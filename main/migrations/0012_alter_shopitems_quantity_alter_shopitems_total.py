# Generated by Django 4.0.5 on 2022-07-06 17:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0011_rename_mail_contact_email'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shopitems',
            name='quantity',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='shopitems',
            name='total',
            field=models.IntegerField(),
        ),
    ]
