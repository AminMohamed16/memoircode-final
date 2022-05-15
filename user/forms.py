from django import forms
from django.contrib.auth.models import User
from .models import Profile
# from .models import Profile


class UserCreationForm(forms.ModelForm):
    username = forms.CharField(max_length=30)
    first_name = forms.CharField()
    last_name = forms.CharField()
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput(), min_length=4)
    Confermpassword = forms.CharField(
        widget=forms.PasswordInput(), min_length=4)

    class Meta:
        model = User
        fields = ('username','first_name','last_name', 'email','password', 'Confermpassword')

    def clean_Confermpassword(self):
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
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ('username', 'password')


class UserUpdateForm(forms.ModelForm):
    first_name = forms.CharField()
    last_name = forms.CharField()
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email')


class ProfilUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('image',)
