# Generated by Django 3.2.5 on 2021-08-02 07:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profileapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='image',
            field=models.ImageField(null=True, upload_to='profile/', verbose_name='사진을 올려보거라'),
        ),
    ]
