from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.forms import ModelForm, TextInput, Textarea, Select, DateInput
from .models import UserProfile, Service, ProcedureRecord, Blog


class SignUpForm(UserCreationForm):
    surname = forms.CharField(
        max_length=25,
        required=True,
        label='Фамилия')

    name = forms.CharField(
        max_length=25,
        required=True,
        label='Имя')

    patronymic = forms.CharField(
        max_length=25,
        required=True,
        label='Отчество')

    phone_number = forms.CharField(
        max_length=15,
        required=True,
        label='Номер телефона')

    class Meta:
        model = User
        fields = ('username', 'surname', 'name', 'patronymic', 'phone_number', 'password1', 'password2')

    def save(self, commit=True):
        user = super(SignUpForm, self).save(commit=False)
        if commit:
            user.save()
            UserProfile.objects.create(
                user=user,
                surname=self.cleaned_data['surname'],
                name=self.cleaned_data['name'],
                patronymic=self.cleaned_data['patronymic'],
                phone_number=self.cleaned_data['phone_number']
            )
        return user


class LoginForm(AuthenticationForm):
    class Meta:
        model = User
        fields = ('username', 'password')


class UpdateInfoForm(forms.ModelForm):   # редактирование информации о пользователе
    surname = forms.CharField(
        max_length=25,
        required=True,
        label='Фамилия')

    name = forms.CharField(
        max_length=25,
        required=True,
        label='Имя')

    patronymic = forms.CharField(
        max_length=25,
        required=True,
        label='Отчество')

    phone_number = forms.CharField(
        max_length=15,
        required=True,
        label='Номер телефона')

    class Meta:
        model = UserProfile
        fields = ('surname', 'name', 'patronymic', 'phone_number')

    def save(self, commit=True):
        profile = super(UpdateInfoForm, self).save(commit=False)
        if commit:
            profile.save()
        return profile


class ServiceForm(forms.ModelForm):   # создание новой услуги
    class Meta:
        model = Service
        fields = ['type', 'name', 'duration', 'price', 'annotation']
        widgets = {
            'type': forms.Select(attrs={'class': 'form-control'}),
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Название услуги'}),
            'duration': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Длитльность процедуры'}),
            'price': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Цена'}),
            'annotation': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Описание'}),
        }


class ProcedureRecordForm(forms.ModelForm):
    class Meta:
        model = ProcedureRecord
        fields = ['client_profile', 'service', 'date', 'time']
        widgets = {
            'client_profile': forms.Select(attrs={'class': 'form-control'}),
            'service': forms.Select(attrs={'class': 'form-control'}),
            'date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'time': forms.TimeInput(attrs={'class': 'form-control', 'type': 'time'}),
        }

    def __init__(self, *args, **kwargs):
        super(ProcedureRecordForm, self).__init__(*args, **kwargs)
        self.fields['service'].queryset = Service.objects.all()


class BlogForm(forms.ModelForm):
    name = forms.CharField(label='Название', widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Название'}))
    notes = forms.CharField(label='Текст записи', widget=forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Текст записи'}))
    image = forms.ImageField(label='Изображение', required=False, widget=forms.FileInput(attrs={'class': 'form-control'}))
    author = forms.CharField(label='Автор', widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Автор'}))

    class Meta:
        model = Blog
        fields = ['name', 'date', 'notes', 'image', 'author']

        widgets = {
            "date": forms.DateInput(attrs={
                'class': 'form-control',
                'type': 'date',
            })
        }

