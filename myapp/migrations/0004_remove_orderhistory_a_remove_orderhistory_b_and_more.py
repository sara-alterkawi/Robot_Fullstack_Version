# Generated by Django 4.2.6 on 2023-12-12 07:15

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("myapp", "0003_alter_user_options"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="orderhistory",
            name="A",
        ),
        migrations.RemoveField(
            model_name="orderhistory",
            name="B",
        ),
        migrations.RemoveField(
            model_name="orderhistory",
            name="C",
        ),
        migrations.RemoveField(
            model_name="orderhistory",
            name="D",
        ),
        migrations.RemoveField(
            model_name="orderhistory",
            name="is_error",
        ),
        migrations.AddField(
            model_name="orderhistory",
            name="sequence",
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name="orderhistory",
            name="error",
            field=models.CharField(blank=True, max_length=120, null=True),
        ),
    ]
