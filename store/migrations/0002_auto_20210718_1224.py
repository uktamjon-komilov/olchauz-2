# Generated by Django 3.2.5 on 2021-07-18 07:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name': 'Category', 'verbose_name_plural': 'Categories'},
        ),
        migrations.RenameField(
            model_name='category',
            old_name='name',
            new_name='category_name',
        ),
    ]
