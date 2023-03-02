from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from .models import Recipe,RecipeIngredients,RecipeInstructions

class RegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)
    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")
        widgets = {
            'username': forms.TextInput(attrs={'class':'form-control'}),
            'email': forms.TextInput(attrs={'class':'form-control'}),
            'password1': forms.PasswordInput(attrs={'class':'form-control'}),
            'password2': forms.PasswordInput(attrs={'class':'form-control'}),
        }

    def save(self, commit=True):
        user = super(RegisterForm, self).save(commit=False)
        user.email = self.cleaned_data["email"]
        if commit:
            user.save()
        return user

class LoginForm(AuthenticationForm):
    class Meta:
        model = User
        fields = ('username', 'password')
        widgets = {
            'username': forms.TextInput(attrs={'class':'form-control'}),
            'password': forms.PasswordInput(attrs={'class':'form-control'}),
        }
    
class RecipeForm(forms.ModelForm):
    class Meta:
        model = Recipe
        #all fields
        fields = ('__all__')

class RecipeIngredientsForm(forms.ModelForm):
    class Meta:
        model = RecipeIngredients
        fields = ('__all__')

class RecipeInstructionsForm(forms.ModelForm):
    class Meta:
        model = RecipeInstructions
        fields = ('__all__')
