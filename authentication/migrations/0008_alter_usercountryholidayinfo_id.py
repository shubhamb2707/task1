# Generated by Django 3.2.7 on 2021-09-29 09:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0007_alter_usercountryholidayinfo_user_uuid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usercountryholidayinfo',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
