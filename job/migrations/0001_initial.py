# Generated by Django 5.1.5 on 2025-01-29 11:24

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rating', models.CharField(choices=[('1', 1), ('2', 2), ('3', 3), ('4', 4), ('5', 5)], default=1, max_length=1)),
                ('description', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone', models.CharField(max_length=11)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Executor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone', models.CharField(max_length=11)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('message_date', models.DateTimeField()),
                ('is_edited', models.BooleanField(default=False)),
                ('description', models.TextField()),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='job.customer')),
                ('executor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='job.executor')),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=99)),
                ('description', models.TextField()),
                ('service_type', models.CharField(choices=[('1', 'Веб разработка'), ('2', 'Дизайн'), ('3', 'Маркетинг'), ('4', 'Копирайтинг'), ('5', 'Рерайтинг'), ('6', 'Видеомонтаж'), ('7', 'Фотошоп')], default=1, max_length=1)),
                ('price', models.IntegerField()),
                ('executor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='job.executor')),
            ],
        ),
        migrations.CreateModel(
            name='Authoring',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('customer', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='job.customer')),
                ('executor', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='job.executor')),
                ('review', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='job.review')),
            ],
        ),
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=99)),
                ('description', models.TextField()),
                ('service_type', models.CharField(choices=[('1', 'Веб разработка'), ('2', 'Дизайн'), ('3', 'Маркетинг'), ('4', 'Копирайтинг'), ('5', 'Рерайтинг'), ('6', 'Видеомонтаж'), ('7', 'Фотошоп')], default=1, max_length=1)),
                ('price', models.IntegerField()),
                ('executor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='job.executor')),
            ],
        ),
        migrations.CreateModel(
            name='Ordering',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order_date', models.DateTimeField()),
                ('deadline', models.DateTimeField()),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='job.customer')),
                ('executor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='job.executor')),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='job.order')),
                ('service', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='job.service')),
            ],
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('order', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='job.order')),
                ('service', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='job.service')),
            ],
        ),
        migrations.CreateModel(
            name='Ticket',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('severity', models.CharField(choices=[('1', 'Низкая'), ('2', 'Cредняя'), ('3', 'Высокая')], default=1, max_length=1)),
                ('description', models.TextField()),
                ('is_resolved', models.BooleanField(default=False)),
                ('customer', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='job.customer')),
                ('executor', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='job.executor')),
            ],
        ),
    ]
