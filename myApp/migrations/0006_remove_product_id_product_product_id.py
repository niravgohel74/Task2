# Generated by Django 4.1.4 on 2024-03-05 09:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("myApp", "0005_alter_category_name"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="product",
            name="id",
        ),
        migrations.AddField(
            model_name="product",
            name="product_id",
            field=models.AutoField(default=1, primary_key=True, serialize=False),
        ),
    ]
