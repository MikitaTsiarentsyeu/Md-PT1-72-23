from django.db import models

class Author(models.Model):

    name = models.CharField(max_length=100)
    email = models.EmailField(primary_key=True)

    def __str__(self) -> str:
        return self.name

class Post(models.Model):

    POST_TYPES = [('c', "copyright"), ('p', "public license")]

    title = models.CharField(max_length=150, blank=True)
    content = models.TextField()
    post_type = models.CharField(max_length=1, choices=POST_TYPES)
    issued = models.DateTimeField()
    image = models.ImageField(upload_to='uploads')

    author = models.ForeignKey('Author', on_delete=models.CASCADE)

