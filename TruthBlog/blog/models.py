from datetime import datetime, timezone
from django.db import models
from django.contrib.auth.models import User


# Create your models here.



class Post(models.Model):

    class Status(models.TextChoices):
        DRAFT = 'DF', 'Draft'
        PUBLISHED = 'PB', 'Published'

    # By default, Django adds an auto-incrementing primary key field to each model.
    title = models.CharField(max_length=250)  # Translates into a VARCHAR column in the SQL database
    
    slug = models.SlugField(max_length=250)   # A slug is a short label that contains only letters, numbers, underscores, or hyphens.
    
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='blog_posts')
    
    body = models.TextField()  # Translates into a TEXT column in the SQL database.
    
    publish = models.DateTimeField(default=datetime.now)  # Translates into a DATETIME column in the SQL database.
    
    created = models.DateTimeField(auto_now_add=True)  # the date will be saved automatically when creating an object.
    
    updated = models.DateTimeField(auto_now=True)  # the date will be saved automatically when saving an object.
    
    status = models.CharField(max_length=2,
                          choices=Status.choices,
                          default=Status.DRAFT)


    # This inner class defines metadata for the model. We use the ordering attribute to tell Django that it should sort results by the publish field. This ordering will apply by default for database queries when no specific order is provided in the query.
    class Meta:
        # We indicate descending order by using a hyphen before the field name, -publish. Posts will be returned in reverse chronological order by default.
        ordering = ['-publish']
        # Adding index to publish field, This will improve performance for queries filtering or ordering results by this field. 
        indexes = [
            models.Index(fields=['-publish']),
        ]

    def __str__(self):      # Default Python method to return a string with the human-readable representation of the object.
        return self.title


