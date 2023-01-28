from django.forms import ModelForm
from .models import Room
from django.contrib.auth.models import User

# This will create a form based on Room table in models.py
class RoomForm(ModelForm):
    class Meta:
        model = Room
        fields = '__all__'
        exclude = ['host', 'participants']  # these fields will not show in the form


class UserForm(ModelForm):
    class Meta:
        model = User
        fields = ['username', 'email']
        