from django.db import models

# Create your models here.
class Book(models.Model):
    book_id   = models.CharField(max_length=10)
    book_name = models.CharField(max_length=50)
    author    = models.CharField(max_length=50)
    publisher = models.CharField(max_length=50)
    status    = models.CharField(max_length=20)

    def __unicode__(self):
        return self.book_name

class User(models.Model):
    user_id       = models.CharField(max_length=20)
    user_name     = models.CharField(max_length=40)
    user_password = models.CharField(max_length=20)
    user_manager  = models.CharField(max_length=40)
    user_admin    = models.CharField(max_length=40)
    user_type     = models.CharField(max_length=20)
    user_tel      = models.DecimalField(max_digits=11, decimal_places=0)
    user_email    = models.EmailField(max_length=40)

    def __unicode__(self):
        return self.user_name

class Record(models.Model):
    user = models.CharField(max_length=20)
    book = models.CharField(max_length=10)
    layout = models.DateField('lend out date')
    returnday = models.DateField('return date')
    class Meta:
        unique_together = (('user', 'book'),)

