from django.db import models

# Create your models here.

class Contact(models.Model):
    name = models.CharField(max_length=250)
    email = models.EmailField(max_length=250)
    subject = models.TextField(max_length=250)
    message = models.TextField()

    def __str__(self):
        return f"{self.name} {self.email} {self.subject} {self.message}"


class Feedback(models.Model):
    name = models.CharField(max_length=250)
    image = models.TextField()
    post = models.CharField(max_length=250)
    comment = models.TextField()

    def __str__(self):
        return f"{self.name} {self.image} {self.post} {self.comment}"