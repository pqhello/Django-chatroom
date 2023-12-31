# Generated by Django 4.2.5 on 2023-09-06 05:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("app1", "0006_alter_userinfo_qqid"),
    ]

    operations = [
        migrations.AlterField(
            model_name="chat_message",
            name="receive_qq",
            field=models.CharField(max_length=15, verbose_name="QQ号"),
        ),
        migrations.AlterField(
            model_name="chat_message",
            name="send_qq",
            field=models.CharField(max_length=15, verbose_name="QQ号"),
        ),
        migrations.AlterField(
            model_name="friend_relation",
            name="qqid",
            field=models.CharField(max_length=15, verbose_name="QQ号"),
        ),
        migrations.AlterField(
            model_name="friend_relation",
            name="qqid_friend",
            field=models.CharField(max_length=15, verbose_name="QQ号"),
        ),
    ]
