from django.db import models


# Create your models here.
# TODO: Create Teacher Class
class Teacher(models.Model):
    title = models.CharField(max_length=10)
    first_name = models.CharField(max_length=25)
    last_name = models.CharField(max_length=25)

    def __str__(self):
        return '%s %s %s' % (self.title, self.first_name, self.last_name)
    pass
