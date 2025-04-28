from django.db import models

class Article(models.Model):
    title = models.CharField(max_length=255)  # Title of the article (required)
    body = models.TextField()  # Body of the article (required)
    # image = models.ImageField(upload_to='images/')  # Uncomment this line if you want to add image support later
    tags = models.JSONField()  # Tags for the article (stored as a JSON array)
    # source = models.CharField(max_length=255, blank=True, null=True)  # Source of the article (optional)

    def __str__(self):
        return self.title