# Generated by Django 2.2.2 on 2019-06-16 09:43

import app.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [("app", "0003_auto_20160820_1607")]

    operations = [
        migrations.AddField(
            model_name="slackuser",
            name="isActive",
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name="mealservice",
            name="untapped",
            field=app.models.JSONField(
                blank=True,
                default=app.models.untapped_default,
                editable=False,
                null=True,
                verbose_name="Untapped",
            ),
        ),
        migrations.AlterField(
            model_name="slackuser",
            name="photo",
            field=models.CharField(default="", max_length=512),
        ),
        migrations.AlterField(
            model_name="slackuser",
            name="user_type",
            field=models.CharField(
                choices=[
                    ("chef", "chef"),
                    ("cleaner", "cleaner"),
                    ("guest", "guest"),
                    ("security", "security"),
                    ("staff", "staff"),
                ],
                default="staff",
                max_length=20,
            ),
        ),
    ]
