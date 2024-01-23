# Generated by Django 5.0 on 2023-12-20 18:49

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Post",
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
                ("title", models.CharField(max_length=1500)),
                ("slug", models.CharField(max_length=1500)),
                ("content", models.TextField()),
                ("image", models.ImageField(blank=True, null=True, upload_to="posts/")),
                (
                    "status",
                    models.CharField(
                        max_length=100,
                        choices=(("production", "Production"), ("staging", "Staging")),
                        default="staging",
                    ),
                ),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
            ],
            options={
                "db_table": "blog_posts",
            },
        ),
    ]
