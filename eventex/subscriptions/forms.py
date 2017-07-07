from django import forms
from django.core.exceptions import ValidationError


def validate_cpf(value):
	if not value.isdigit():
		raise ValidationError('CPF deve conter apenas números', 'cpf_digits')
	if len(value) != 11:
		raise ValidationError('CPF deve ter 11 digitos', 'cpf_length')

class SubscriptionForm(forms.Form):
	name = forms.CharField(label='Nome')
	cpf = forms.CharField(label='CPF', max_length=11, validators=[validate_cpf])
	email = forms.EmailField(label='Email')
	phone = forms.CharField(label='Telefone')