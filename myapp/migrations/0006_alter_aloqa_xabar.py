# Generated by Django 4.0.3 on 2022-04-22 06:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0005_aloqa'),
    ]

    operations = [
        migrations.AlterField(
            model_name='aloqa',
            name='xabar',
            field=models.CharField(max_length=300, null=True),
        ),
    ]
