# Generated by Django 4.1.6 on 2023-02-04 04:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("home", "0006_alter_userinfo_profile_picture"),
    ]

    operations = [
        migrations.AlterField(
            model_name="picture",
            name="picture_random_code",
            field=models.CharField(default="0W9bAYH4PN", max_length=20),
        ),
        migrations.AlterField(
            model_name="userinfo",
            name="profile_picture",
            field=models.ImageField(
                default="media/photos/7yC1YMYtzT.svg", upload_to="user_images"
            ),
        ),
    ]
