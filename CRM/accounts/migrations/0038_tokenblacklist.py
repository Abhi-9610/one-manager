# Generated by Django 4.2.7 on 2023-11-29 11:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0037_delete_tokenblacklist'),
    ]

    operations = [
        migrations.CreateModel(
            name='TokenBlacklist',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('token', models.CharField(max_length=255, unique=True)),
            ],
        ),
    ]
