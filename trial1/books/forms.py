from django import forms


class BookForm(forms.Form):
    name = forms.CharField(max_length=20)
    description = forms.CharField(max_length=20)


class Login(forms.Form):
    username = forms.CharField(max_length=20)
    password = forms.CharField(label='password', widget=forms.PasswordInput(attrs={'placeholder': 'Password'}))

