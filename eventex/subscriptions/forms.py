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


	#Inicia nome com letra maiuscula
	def clean_name(self):
		name = self.cleaned_data['name']
		self.cleaned_data['name'] = name.title()
		#words = [w.capitalize() for w in name.split()]
		# return ' '.join(words)
		return self.cleaned_data['name']
