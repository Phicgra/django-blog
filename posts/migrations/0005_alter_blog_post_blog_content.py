# Generated by Django 4.2.15 on 2024-10-23 19:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0004_rename_aurthor_blog_post_author'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog_post',
            name='blog_content',
            field=models.TextField(default='Your of your Post', max_length=10000),
        ),
    ]