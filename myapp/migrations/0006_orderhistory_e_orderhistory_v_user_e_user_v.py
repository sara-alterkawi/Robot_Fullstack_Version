# Generated by Django 4.2.6 on 2023-12-17 20:34

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("myapp", "0005_remove_orderhistory_sequence_orderhistory_a_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="orderhistory",
            name="E",
            field=models.IntegerField(default=None, null=True),
        ),
        migrations.AddField(
            model_name="orderhistory",
            name="V",
            field=models.IntegerField(default=None, null=True),
        ),
        migrations.AddField(
            model_name="user",
            name="E",
            field=models.IntegerField(default=10),
        ),
        migrations.AddField(
            model_name="user",
            name="V",
            field=models.IntegerField(default=10),
        ),
    ]
