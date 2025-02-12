# Generated by Django 5.1.5 on 2025-02-01 05:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('job', '0003_rename_service_type_order_order_type_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='service',
            name='description_en',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='service',
            name='description_ky',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='service',
            name='description_ru',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='service',
            name='name_en',
            field=models.CharField(max_length=99, null=True),
        ),
        migrations.AddField(
            model_name='service',
            name='name_ky',
            field=models.CharField(max_length=99, null=True),
        ),
        migrations.AddField(
            model_name='service',
            name='name_ru',
            field=models.CharField(max_length=99, null=True),
        ),
    ]
