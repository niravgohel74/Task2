# Generated by Django 4.1.4 on 2024-03-05 08:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("myApp", "0002_remove_product_id_product_product_id"),
    ]

    operations = [
        migrations.AlterField(
            model_name="product",
            name="product_id",
            field=models.AutoField(default=1, primary_key=True, serialize=False),
        ),
    ]
