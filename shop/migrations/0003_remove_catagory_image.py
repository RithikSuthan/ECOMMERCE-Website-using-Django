# Generated by Django 4.1.1 on 2022-10-09 10:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0002_remove_product_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='catagory',
            name='image',
        ),
    ]
