# Generated by Django 4.2.6 on 2023-12-17 21:04

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("myapp", "0006_orderhistory_e_orderhistory_v_user_e_user_v"),
    ]

    operations = [
        migrations.RenameField(
            model_name="orderhistory",
            old_name="V",
            new_name="F",
        ),
        migrations.RenameField(
            model_name="user",
            old_name="V",
            new_name="F",
        ),
        migrations.AddField(
            model_name="orderhistory",
            name="G",
            field=models.IntegerField(default=None, null=True),
        ),
        migrations.AddField(
            model_name="orderhistory",
            name="H",
            field=models.IntegerField(default=None, null=True),
        ),
        migrations.AddField(
            model_name="user",
            name="G",
            field=models.IntegerField(default=10),
        ),
        migrations.AddField(
            model_name="user",
            name="H",
            field=models.IntegerField(default=10),
        ),
    ]
