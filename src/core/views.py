from crispy_forms.bootstrap import FormActions
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Field, Submit
from django.shortcuts import render
from .models import *
from django import forms
from django.contrib.auth.models import AbstractUser
from django.views.generic.edit import FormView
from django.contrib.auth.forms import UserCreationForm


class RegistrationForm(UserCreationForm):
    first_name = forms.CharField(required=False)
    class Meta:
        model = User
        fields = ('first_name', 'username', 'password1', 'password2')

class RegisterFormView(FormView):
    helper = FormHelper()
    helper.form_tag = False
    helper.form_show_labels = False
    form_class = RegistrationForm

    # Ссылка, на которую будет перенаправляться пользователь в случае успешной регистрации.
    # В данном случае указана ссылка на страницу входа для зарегистрированных пользователей.
    success_url = "/users/login/"

    # Шаблон, который будет использоваться при отображении представления.
    template_name = "core/register.html"

    def form_valid(self, form):
        # Создаём пользователя, если данные в форму были введены корректно.
        form.save()

        # Вызываем метод базового класса
        return super(RegisterFormView, self).form_valid(form)