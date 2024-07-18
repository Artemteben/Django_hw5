# Generated by Django 5.0.7 on 2024-07-18 18:09

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Category",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "name",
                    models.CharField(
                        max_length=100, verbose_name="Наименование категории"
                    ),
                ),
                (
                    "description",
                    models.TextField(
                        blank=True, null=True, verbose_name="Описание категории"
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Product",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=100, verbose_name="Наименование")),
                (
                    "image",
                    models.ImageField(
                        blank=True,
                        max_length=150,
                        null=True,
                        upload_to="",
                        verbose_name="Изображение",
                    ),
                ),
                (
                    "category",
                    models.CharField(max_length=150, verbose_name="Категория"),
                ),
                ("price", models.IntegerField(verbose_name="Цена за покупку")),
                (
                    "created_at",
                    models.DateField(max_length=150, verbose_name="Дата создания"),
                ),
                (
                    "updated_at",
                    models.DateField(
                        max_length=150, verbose_name="Дата последнего изменения"
                    ),
                ),
                (
                    "description",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="products",
                        to="catalog.category",
                        verbose_name="Описание",
                    ),
                ),
            ],
            options={
                "verbose_name": "продукт",
                "verbose_name_plural": "продукты",
            },
        ),
    ]