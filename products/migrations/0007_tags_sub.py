# Generated by Django 3.1.7 on 2021-04-04 05:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0006_subtags'),
    ]

    operations = [
        migrations.AddField(
            model_name='tags',
            name='sub',
            field=models.BooleanField(default=False),
        ),
    ]
