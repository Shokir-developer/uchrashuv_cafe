# Generated by Django 4.0.3 on 2022-04-22 04:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_yeguliklar'),
    ]

    operations = [
        migrations.AddField(
            model_name='yeguliklar',
            name='nomi',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='category',
            name='name',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
