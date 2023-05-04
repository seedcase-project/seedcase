# Generated by Django 4.1.2 on 2023-04-27 13:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base_app', '0002_remove_project_project_team_project_team_member_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Token',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_name', models.CharField(help_text='This identifies the user which will be using this token.', max_length=255, unique=True)),
                ('token', models.CharField(help_text='The access token, a random string. ', max_length=32, unique=True)),
                ('token_associated_app', models.CharField(blank=True, choices=[('project_app', 'importing data to the project')], default='exporting', help_text='This identifies the APP which will be using this token.', max_length=255, null=True)),
            ],
        ),
    ]
