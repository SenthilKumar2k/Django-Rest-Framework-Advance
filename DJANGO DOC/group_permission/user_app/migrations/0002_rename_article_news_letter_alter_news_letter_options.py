# Generated by Django 5.1.4 on 2024-12-10 12:12

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user_app', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Article',
            new_name='News_letter',
        ),
        migrations.AlterModelOptions(
            name='news_letter',
            options={'permissions': [('publish_newsletter', 'can publish an newsletter'), ('unpublish_newsletter', 'can unpublish an newsletter'), ('edit_newsletter', 'can edit an newsletter'), ('review_newsletter', 'can review an newsletter')]},
        ),
    ]
