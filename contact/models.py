from django.db import models


class Contact(models.Model):
    """ 
    contact model
    """
    name                    = models.CharField(max_length=150)
    email                   = models.EmailField()
    subject                 = models.CharField(max_length=150)
    message                 = models.TextField()

    def __str__(self):
        return self.subject

