# Generated by Django 4.1.2 on 2023-06-07 08:44

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("base_app", "0004_alter_uploadedfile_file"),
    ]

    operations = [
        migrations.RenameModel(
            old_name="UploadedFile",
            new_name="DataFile",
        ),
        migrations.AlterModelOptions(
            name="datafile",
            options={"verbose_name": "data_file", "verbose_name_plural": "data_files"},
        ),
    ]
