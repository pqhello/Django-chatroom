# Generated by Django 4.2.5 on 2023-09-05 09:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("app1", "0002_alter_qq_andpassword_qqid"),
    ]

    operations = [
        migrations.RemoveField(model_name="userinfo", name="depart",),
    ]
