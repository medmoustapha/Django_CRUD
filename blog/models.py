from django.db import models

# Create your models here.
class Author(models.Model):
    first_name=models.CharField(max_length=40)
    last_name=models.CharField(max_length=40)
    email=models.EmailField()
    phone=models.CharField(max_length=12)

    def __str__(self):
        return self.first_name+" "+self.last_name
class Article(models.Model):
   
    title=models.CharField(max_length=120)
    content=models.TextField()
    #Many to One
    author=models.ForeignKey(Author,on_delete=models.CASCADE)
    def __str__(self):
        return self.title