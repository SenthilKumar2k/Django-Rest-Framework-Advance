from django.db import models

# Create your models here.
class News_letter(models.Model):
    title=models.CharField(max_length=225)
    content=models.TextField()
    user=models.ForeignKey('auth.User', on_delete=models.CASCADE)

    # Adding Custom Permissions to a Model
    class Meta:
        permissions=[
            ('publish_newsletter', 'can publish an newsletter'), # codename, A human-readable name
            ('unpublish_newsletter', 'can unpublish an newsletter'),
            ('edit_newsletter', 'can edit an newsletter'),
            ('review_newsletter', 'can review an newsletter')
        ]
#When you run makemigrations and migrate, these permissions are added to the auth_permission table.