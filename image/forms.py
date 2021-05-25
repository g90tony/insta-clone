from django import forms
from cloudinary.models import CloudinaryField
from django.db.models.fields import CharField, TextField

class NewImageForm(forms.Form):
    new_image = CloudinaryField('image', default=None)
    image_caption = TextField()
    image_name = CharField()