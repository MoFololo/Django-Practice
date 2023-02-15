# Generated by Django 4.1.5 on 2023-02-08 15:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("polls", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Comment",
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
                ("title_text", models.CharField(max_length=200)),
                ("comment_text", models.CharField(max_length=200)),
                ("pub_date", models.DateTimeField(verbose_name="date published")),
            ],
        ),
    ]
