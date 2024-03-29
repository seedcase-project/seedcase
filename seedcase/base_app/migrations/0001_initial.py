# Generated by Django 4.1.2 on 2022-10-13 11:44

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="Organization",
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
                ("time_created", models.DateTimeField(auto_now_add=True)),
                ("time_modified", models.DateTimeField(auto_now=True, null=True)),
                (
                    "address",
                    models.CharField(
                        blank=True,
                        max_length=128,
                        null=True,
                        verbose_name="Address line 1",
                    ),
                ),
                (
                    "address2",
                    models.CharField(
                        blank=True,
                        max_length=128,
                        null=True,
                        verbose_name="Address line 2",
                    ),
                ),
                ("city", models.CharField(blank=True, max_length=32, null=True)),
                (
                    "province",
                    models.CharField(
                        blank=True,
                        help_text="Full province name",
                        max_length=32,
                        null=True,
                    ),
                ),
                ("postal_code", models.CharField(blank=True, max_length=16, null=True)),
                (
                    "country",
                    models.CharField(
                        blank=True,
                        help_text="ISO 3166-1 two-letter country code",
                        max_length=2,
                        null=True,
                    ),
                ),
                ("name", models.CharField(max_length=150, unique=True)),
                ("note", models.TextField(blank=True, max_length=500, null=True)),
                (
                    "last_modified_by",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="%(app_label)s_%(class)s_related",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Project",
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
                ("time_created", models.DateTimeField(auto_now_add=True)),
                ("time_modified", models.DateTimeField(auto_now=True, null=True)),
                ("name", models.CharField(max_length=150, unique=True)),
                (
                    "description",
                    models.TextField(blank=True, max_length=500, null=True),
                ),
                (
                    "last_modified_by",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="%(app_label)s_%(class)s_related",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
                (
                    "project_team",
                    models.ManyToManyField(blank=True, to=settings.AUTH_USER_MODEL),
                ),
                (
                    "stakeholder",
                    models.ManyToManyField(blank=True, to="base_app.organization"),
                ),
            ],
            options={
                "verbose_name": "Project",
                "verbose_name_plural": "Projects",
            },
        ),
        migrations.CreateModel(
            name="OrganizationType",
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
                ("time_created", models.DateTimeField(auto_now_add=True)),
                ("time_modified", models.DateTimeField(auto_now=True, null=True)),
                ("name", models.CharField(max_length=30, unique=True)),
                (
                    "description",
                    models.CharField(blank=True, max_length=200, null=True),
                ),
                (
                    "last_modified_by",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="%(app_label)s_%(class)s_related",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
            options={
                "verbose_name": "Organization Type",
                "verbose_name_plural": "Organization Types",
            },
        ),
        migrations.AddField(
            model_name="organization",
            name="types",
            field=models.ManyToManyField(blank=True, to="base_app.organizationtype"),
        ),
        migrations.AlterUniqueTogether(
            name="organization",
            unique_together={
                (
                    "name",
                    "address",
                    "address2",
                    "city",
                    "province",
                    "country",
                    "postal_code",
                )
            },
        ),
    ]
