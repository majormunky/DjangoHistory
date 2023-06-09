# Generated by Django 4.1.7 on 2023-03-27 05:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("home", "0003_alter_edition_page_count"),
    ]

    operations = [
        migrations.CreateModel(
            name="Page",
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
                ("page_num", models.IntegerField()),
                ("url", models.URLField(blank=True)),
                ("is_downloaded", models.BooleanField(default=False)),
                (
                    "edition",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="home.edition"
                    ),
                ),
            ],
        ),
    ]
