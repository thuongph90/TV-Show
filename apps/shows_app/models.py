from django.db import models
from datetime import date,datetime
class BlogManager(models.Manager):
    def basic_validator(self,postData):
        errors={}
        print(postData['title'])
        print('kkkkkkkkkkkkkkkkkkkkk')
        print(postData['released_date'])
        
        
        if len(postData['title'])<2:
            errors['title']="Title should be at least 2 characters"
        if len(postData['network'])<1:
            errors["network"]="network should be at least 2 characters"
         # 'network' should be match to input 'network' in html, not from class: shows
        if len(postData['description'])<10:
            errors["description"]="Description is optional but it should be at least 10 characters"
            # 'description' should be match to input 'description' in html, not from class: shows
        # if datetime.strftime('postData['released_date']','%Y %b %d')>date.today():
        #     errors["released_date"]="released_date should be in the past"
        
        return errors
class shows(models.Model):
    title = models.CharField(max_length=255)
    network=models.CharField(max_length=255)
    released_date = models.DateTimeField()
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects=BlogManager()

