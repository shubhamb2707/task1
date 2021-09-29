# Generated by Django 3.2.7 on 2021-09-28 03:12

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0001_initial'),
        ('authentication', '0002_post'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='likecount',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='post',
            name='unlikecount',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.CreateModel(
            name='LikeUnlike',
            fields=[
                ('basemodel_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='base.basemodel')),
                ('Like', models.BooleanField(default=False)),
                ('Unlike', models.BooleanField(default=False)),
                ('post_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='authentication.post')),
                ('user_of', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            bases=('base.basemodel',),
        ),
    ]
