from .models import Review, Contacts, Feedback
from django.forms import ModelForm, TextInput, Textarea, EmailInput, NumberInput, ImageField
from django import forms



class ReviewForm(ModelForm):
    class Meta:
        model = Review
        fields = ["name", "age", "image", "email", "tel", "review"]
        widgets = {
            "name": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введите Имя'
            }),
            "age": NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'Возраст'
            }),
            "email": EmailInput(attrs={
                'class': 'form-control',
                'placeholder': 'email'
            }),
            "tel": TextInput(attrs={
                'class': 'form-control',
                'placeholder': '+(375)29-555-55-55'
            }),
            "review": Textarea(attrs={
                'cols': 70, 'rows': 10,
                'class': 'form-control',
                'placeholder': 'Оставьте свой отзыв'
            }),
        }


class FeedbackForm(ModelForm):
    class Meta:
        model = Feedback
        fields = ["name", "tel", "email", "theme", "contact"]
        widgets = {
            "name": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Ваше имя'
            }),
            "tel": TextInput(attrs={
                'class': 'form-control',
                'placeholder': '+(375)29-555-55-55'
            }),
            "email": EmailInput(attrs={
                'class': 'form-control',
                'placeholder': 'email'
            }),
            "theme": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Тема вопроса'
            }),
            "contact": Textarea(attrs={
                'cols': 70, 'rows': 10,
                'class': 'form-control',
                'placeholder': 'Напишите свой вопрос'
            }),
        }

