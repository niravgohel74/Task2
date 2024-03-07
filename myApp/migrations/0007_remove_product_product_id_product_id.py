# Generated by Django 4.1.4 on 2024-03-05 10:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("myApp", "0006_remove_product_id_product_product_id"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="product",
            name="product_id",
        ),
        migrations.AddField(
            model_name="product",
            name="id",
            field=models.BigAutoField(
                auto_created=True,
                
                primary_key=True,
                serialize=False,
                verbose_name="ID",
            ),
            preserve_default=False,
        ),
    ]