from django.db import models


class Book(models.Model):
    
   book_cover = models.CharField(max_length=50)
   book_author = models.CharField(max_length=50,default='abc')
   publisher = models.CharField(max_length=50,default='def')
   published_year = models.IntegerField(default=123)
  
   def __str__(self):
       return self.book_cover



