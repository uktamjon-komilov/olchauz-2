# Generated by Django 3.2.5 on 2021-07-18 07:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0004_auto_20210718_1234'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='sub_cateogry',
            new_name='sub_category',
        ),
    ]
