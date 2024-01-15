# Generated by Django 4.2.6 on 2023-12-19 23:03

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("myapp", "0009_remove_orderhistory_status"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="user",
            options={"verbose_name": "user", "verbose_name_plural": "users"},
        ),
        migrations.AddField(
            model_name="orderhistory",
            name="status",
            field=models.CharField(default="pending", max_length=100),
        ),
        migrations.AlterField(
            model_name="orderhistory",
            name="A",
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name="orderhistory",
            name="B",
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name="orderhistory",
            name="C",
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name="orderhistory",
            name="D",
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name="orderhistory",
            name="E",
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name="orderhistory",
            name="F",
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name="orderhistory",
            name="G",
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name="orderhistory",
            name="H",
            field=models.IntegerField(blank=True, null=True),
        ),
    ]