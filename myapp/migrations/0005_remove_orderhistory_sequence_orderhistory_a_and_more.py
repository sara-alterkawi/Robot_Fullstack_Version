# Generated by Django 4.2.6 on 2023-12-12 09:24

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("myapp", "0004_remove_orderhistory_a_remove_orderhistory_b_and_more"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="orderhistory",
            name="sequence",
        ),
        migrations.AddField(
            model_name="orderhistory",
            name="A",
            field=models.IntegerField(default=None, null=True),
        ),
        migrations.AddField(
            model_name="orderhistory",
            name="B",
            field=models.IntegerField(default=None, null=True),
        ),
        migrations.AddField(
            model_name="orderhistory",
            name="C",
            field=models.IntegerField(default=None, null=True),
        ),
        migrations.AddField(
            model_name="orderhistory",
            name="D",
            field=models.IntegerField(default=None, null=True),
        ),
        migrations.AddField(
            model_name="orderhistory",
            name="is_error",
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name="orderhistory",
            name="error",
            field=models.CharField(default=None, max_length=120, null=True),
        ),
    ]
