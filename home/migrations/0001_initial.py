# Generated by Django 4.1.6 on 2023-02-03 13:19

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
            name="Picture",
            fields=[
                ("picture_id", models.AutoField(primary_key=True, serialize=False)),
                ("picture_like", models.IntegerField()),
                ("picture_random_code", models.BigIntegerField()),
                ("pic", models.ImageField(upload_to="photos")),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
            options={
                "verbose_name": "Picture",
                "verbose_name_plural": "Pictures",
            },
        ),
        migrations.CreateModel(
            name="UserInfo",
            fields=[
                ("user_info_id", models.AutoField(primary_key=True, serialize=False)),
                ("profile_picture", models.ImageField(upload_to="user_images")),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
                ("user_pic", models.ManyToManyField(to="home.picture")),
            ],
            options={
                "verbose_name": "UserInfo",
                "verbose_name_plural": "UserInfos",
            },
        ),
    ]