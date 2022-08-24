from django.forms import ModelForm, Textarea, widgets, TextInput
from .models import Book, User

class RegForm(ModelForm):
    class Meta:
        model = User
        fields = '__all__'
        labels = {
            'first_name': ('Your First Name'),
        }
        error_messages = {
            'first_name': {
                'min_length': ("First name must be at least 2 characters long."),
            },
        }
        widgets = {
            'password': widgets.PasswordInput,
        }
        
class LoginForm(ModelForm):
    class Meta:
        model= User
        fields = ['email', 'password']
        widgets = {
            'password': widgets.PasswordInput,
        }

class NewBookForm(ModelForm):
    class Meta:
        model= Book
        fields= '__all__'
        widgets = {
            'description': Textarea(attrs={'cols': 60, 'rows': 20}),
        }