# Generated by Django 4.1 on 2024-06-04 00:43

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("Users", "0003_alter_users_user_enteryear"),
    ]

    operations = [
        migrations.AddField(
            model_name="users",
            name="is_active",
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name="users",
            name="is_staff",
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name="users",
            name="is_superuser",
            field=models.BooleanField(default=False),
        ),
    ]
