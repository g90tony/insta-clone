from django.db import models
from cloudinary.models import CloudinaryField
from django.contrib.postgres.fields import ArrayField
from django.db.models.deletion import CASCADE

# Create your models here.

class Profile(models.Model):
    profile_photo = CloudinaryField('image', default = None)
    bio = models.TextField()
    user_name = models.CharField(max_length=255)  
    followers = ArrayField(models.IntegerField())
    following = ArrayField(models.IntegerField())
    joined = models.DateField(auto_now_add=True)
    
    
    def save_profile(self):
        self.save()
        
    def update_profile(self, profile_id, update_profile_image): 
        self.objects(id = profile_id).update(profile_photo = update_profile_image)
    
    def update_bio(self, profile_id, update_profile_bio): 
        self.objects(id = profile_id).update(bio = update_profile_bio)
        
    def delete_profile(self):
        self.objects.delete()
    
    def __str__(self):
        return self.user_name
        

class Image(models.Model):
    image = CloudinaryField('image', default= None)
    image_name = models.CharField(max_length=255)
    image_caption = models.CharField(max_length=255)
    profile_id = models.ForeignKey(Profile , on_delete=CASCADE)
    likes = models.IntegerField()
    created_at = models.DateField(auto_now_add=True)
    
    def save_image(self):
        self.save()
        
    def delete_image(self):
        self.delete()
        
    def update_caption(self, image_id, new_caption):
        self.objects.filter(id = image_id).update(image_caption = new_caption)
        
    def __str__(self):
        return self.image_name
    
    
class Comment(models.Model):
    image = models.ForeignKey(Image, on_delete=CASCADE)
    profile = models.ForeignKey(Profile, on_delete=CASCADE)
    created_on = models.DateField(auto_now_add=True)
    content = models.TextField()
    
    def save_comment(self):
        self.save()
        
    def __str__(self):
        return self.create_on