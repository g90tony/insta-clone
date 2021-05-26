from django.db.models import fields
from .models import Profile, Image
from django import forms
from cloudinary.models import CloudinaryField
from django.forms.widgets import Textarea


class NewImageForm(forms.Form):
    new_image = forms.FileField()
    image_caption = forms.CharField( max_length=255, required=False, widget=Textarea)
    
    class Meta:
        model = Image
        fields = ('new_image','image_caption')
    
class NewProfileForm(forms.Form):
    profile_photo = forms.FileField()
    bio = forms.CharField( max_length=255, required=False, widget=Textarea)
    
    class Meta:
        model = Profile
        fields = ('profile_photo', 'bio')