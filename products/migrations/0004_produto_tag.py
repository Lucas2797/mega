# Generated by Django 3.1.7 on 2021-04-02 00:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0003_remove_tags_product'),
    ]

    operations = [
        migrations.AddField(
            model_name='produto',
            name='tag',
            field=models.ManyToManyField(to='products.Tags'),
        ),
    ]