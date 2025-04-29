from django.db import models

class Article(models.Model):
    title = models.CharField(max_length=255)  # Title of the article (required)
    body = models.TextField()  # Body of the article (required)
    # image = models.ImageField(upload_to='images/')  # Uncomment this line if you want to add image support later
    tags = models.JSONField()  # Tags for the article (stored as a JSON array)
    # source = models.CharField(max_length=255, blank=True, null=True)  # Source of the article (optional)

    def __str__(self):
        return self.title
class User(models.Model):
    username = models.CharField(max_length=255, unique=True)  # Username (unique)
    password = models.CharField(max_length=255)  # Password (hashed)
    email = models.EmailField(max_length=255, unique=True)  # Email (unique)
    created_at = models.DateTimeField(auto_now_add=True)  # Timestamp when the user was created
    is_active = models.BooleanField(default=True)  # Indicates if the user is active

    def __str__(self):
        return self.username
class API_keys(models.Model):
    key = models.CharField(max_length=255, unique=True)  # API key (unique)
    created_at = models.DateTimeField(auto_now_add=True)  # Timestamp when the key was created
    is_active = models.BooleanField(default=True)  # Indicates if the key is active
    owner = models.OneToOneField(User, on_delete=models.CASCADE)  # Foreign key to the UserModel

    def __str__(self):
        return self.key