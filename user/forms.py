from django import forms
from django.contrib.auth.models import User
# from .models import Profile


class UserCreationForm(forms.ModelForm):
    username = forms.CharField(max_length=30)
    email = forms.EmailField()
    first_name = forms.CharField()
    last_name = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput(), min_length=4)
    Confermpassword = forms.CharField(widget=forms.PasswordInput(), min_length=4)

    class Meta:
        model = User
        fields = ('username', 'email', 'first_name',
                    'last_name', 'password', 'Confermpassword')

    def clean_password2(self):
        cd = self.cleaned_data
        if cd['password'] != cd['Confermpassword']:
            raise forms.ValidationError('كلمة المرور غير متطابقة')
        return cd['Confermpassword']

    def clean_username(self):
        cd = self.cleaned_data
        if User.objects.filter(username=cd['username']).exists():
            raise forms.ValidationError('يوجد مستخدم مسجل بهذا الاسم.')
        return cd['username']

class LoginForm(forms.ModelForm):
    username=forms.CharField()
    password =forms.CharField(widget=forms.PasswordInput())
    class Meta:
        model = User
        fields = ('username','password')