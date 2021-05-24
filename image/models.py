from django.db import models
from cloudinary.models import CloudinaryField
from django.db.models.base import Model
# Create your models here.

class Profile(models.Model):
    profile_photo = CloudinaryField('image', default = None)
    bio = models.TextField()
    
    def save_profile(self):
        self.save()
        
    def update_profile(self, profile_id, update_profile_image): 
        self.objects(id = profile_id).update(profile_photo = update_profile_image)
    
    def update_bio(self, profile_id, update_profile_bio): 
        self.objects(id = profile_id).update(bio = update_profile_bio)
        
    def delete_profile(self, profile_id):
        self.objects.delete()
        

class Image(models.Model):
    image = CloudinaryField('image', default= None)
    image_name = models.CharField()
    image_caption = models.CharField()
    profile_id = models.ForeignKey(Profile)
    likes = models.IntegerField()
    
    def save_image(self):
        self.save()
        
    def delete_image(self):
        self.delete()
        
    def update_caption(self, image_id, new_caption):
        self.objects.filter(id = image_id).update(image_caption = new_caption)