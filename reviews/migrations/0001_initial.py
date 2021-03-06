# Generated by Django 2.2.16 on 2021-12-02 16:31

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField(verbose_name='text')),
                ('pub_date', models.DateTimeField(auto_now_add=True, db_index=True, verbose_name='date_published')),
            ],
        ),
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField(verbose_name='text')),
                ('score', models.PositiveIntegerField(default=5, null=True, validators=[django.core.validators.MaxValueValidator(10, message='Введите целое число от 1 до 10'), django.core.validators.MinValueValidator(1, message='Введите целое число от 1 до 10')], verbose_name='review-score')),
                ('pub_date', models.DateTimeField(auto_now_add=True, db_index=True, verbose_name='date_published')),
            ],
            options={
                'verbose_name_plural': 'Reviews',
                'ordering': ('-pub_date',),
            },
        ),
    ]
