from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django import forms
from mailing.forms import StyleFormsMixin

from users.models import User


class RegisterForm(StyleFormsMixin, UserCreationForm):

    class Meta:
        model = User
        fields = ["email", "password1", "password2"]

    def label_from_instance(self, obj):
        if self.fields["password1"]:
            self.fields["password1"].label = "Пароль"
        if self.fields["password2"]:
            self.fields["password2"].label = "Подтверждение пароля"

        return super().label_from_instance(obj)


class UpdateForm(StyleFormsMixin, UserChangeForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["password"].widget = forms.HiddenInput()

    class Meta:
        model = User
        fields = ["first_name", "last_name", "email", "num_phone", "avatar", "country"]
