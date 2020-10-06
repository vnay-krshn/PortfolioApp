from django.db import models

# Create your models here.

class Projects(models.Model):
    image = models.ImageField(upload_to = 'images/')
    summary = models.CharField(max_length=500)

    # __str__ is an in-built python function used for string representation of objects
    # self is current instance of the class and allows to access the objects and methods of the class
    def __str__(self):
        return self.summary
