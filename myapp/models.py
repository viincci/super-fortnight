from django.db import models
#from imagekit.models import ProcessedImageField
#from imagekit.processors import ResizeToFit
from django.utils.translation import gettext as _

# Create your models here.
class Categories(models.Model):
    cat_id = models.IntegerField(primary_key=True,unique=True)
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=200)
   
    def __str__(self) :
        return self.name



class Award(models.Model):
    title = models.CharField(max_length=70)
    description = models.TextField(max_length=1024, null=True, blank=True)
    Image =models.ImageField(_(""), upload_to="media", height_field=None, width_field=None, max_length=None)
    Year = models.IntegerField()
    category = models.ForeignKey(Categories,on_delete=models.CASCADE,null=True,blank=True)
    Position = models.CharField(max_length=50)

    
    
    def imageURL(self):
        try:
            url = self.Image.url
        except:
            url = ''
        return url
    
    def __str__(self):
        return self.title

class Service(models.Model):
    title = models.CharField(max_length=70)
    description = models.TextField(max_length=1024)
    Image =models.ImageField(_(""), upload_to="media", height_field=None, width_field=None, max_length=None)
    thumb = models.ImageField(_(""), upload_to="media", height_field=None, width_field=None, max_length=None)
    def imageURL(self):
        try:
            url = self.Image.url
        except:
            url = ''
        return url 
    def thumbURL(self):
        try:
            url = self.thumb.url
        except:
            url = ''
        return url

    def __str__(self):
        return self.title




class Reference(models.Model):
    name = models.CharField(max_length=70)
    occupation = models.TextField(max_length=1024)
    Qoute = models.TextField(max_length=1024)

    def __str__(self):
        return self.name