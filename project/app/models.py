from django.db import models

class Quote(models.Model):
    quote = models.CharField(max_length=10000,null=True,blank=True)
    movie_title = models.CharField(max_length=10000,null=True,blank=True)
    #Real actor name   e.g Vin Disel
    actor_name    = models.CharField(max_length=10000,null=True,blank=True) 
    category      = models.CharField(max_length=10000,null=True,blank=True) 
    publish_date  = models.CharField(max_length=10000,null=True,blank=True) 
    source        = models.CharField(max_length=10000,null=True,blank=True) 
    context       = models.CharField(max_length=10000,null=True,blank=True) 
    rating        = models.CharField(max_length=10000,null=True,blank=True) 
    language      = models.CharField(max_length=10000,null=True,blank=True) 
    #Name of action inside move e.g Domenic Torreto
    author        = models.CharField(max_length=10000,null=True,blank=True) 
    #include a short description of the author of the quote
    author_bio    = models.CharField(max_length=10000,null=True,blank=True) 
    #user_rating


    # secretIdentity = models.CharField(max_length=100)

    def __str__(self):
        return self.quote
