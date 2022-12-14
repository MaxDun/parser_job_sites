# Generated by Django 3.2.6 on 2022-10-07 06:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('job', '0004_auto_20221004_1931'),
    ]

    operations = [
        migrations.CreateModel(
            name='Job',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField(max_length=250)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('source', models.CharField(choices=[('dou', 'dou'), ('other', 'other')], default='other', max_length=250)),
                ('url', models.URLField(max_length=250, unique=True)),
                ('salary_info', models.TextField(max_length=250, null=True)),
                ('place_info', models.TextField(max_length=250, null=True)),
            ],
        ),
        migrations.DeleteModel(
            name='Post',
        ),
    ]
