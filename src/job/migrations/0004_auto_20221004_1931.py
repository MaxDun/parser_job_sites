# Generated by Django 3.2.6 on 2022-10-04 19:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('job', '0003_alter_post_source'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='place_info',
            field=models.TextField(max_length=250, null=True),
        ),
        migrations.AddField(
            model_name='post',
            name='salary_info',
            field=models.TextField(max_length=250, null=True),
        ),
        migrations.AlterField(
            model_name='post',
            name='url',
            field=models.URLField(max_length=250, unique=True),
        ),
    ]
