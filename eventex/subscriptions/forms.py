from django import forms
from django.core.exceptions import ValidationError
from eventex.subscriptions.models import Subscription
from eventex.subscriptions.validators import validate_cpf


class SubscriptionFormOld(forms.Form):
	name = forms.CharField(label='Nome')
	cpf = forms.CharField(label='CPF', max_length=11, validators=[validate_cpf])
	email = forms.EmailField(label='Email', required=False)
	phone = forms.CharField(label='Telefone', required=False)

	#Inicia nome com letra maiuscula
	def clean_name(self):
		name = self.cleaned_data['name']
		self.cleaned_data['name'] = name.title()
		#words = [w.capitalize() for w in name.split()]
		# return ' '.join(words)
		return self.cleaned_data['name']

	#Retorno depois que validou o formulario
	def clean(self):
		if not self.cleaned_data.get('email') and not self.cleaned_data.get('phone'):
			raise ValidationError('Informe email ou telefone.')
		return self.cleaned_data


class SubscriptionForm(forms.ModelForm):

	class Meta:
		model = Subscription
		fields = ['name', 'cpf', 'email', 'phone']

	# Inicia nome com letra maiuscula
	def clean_name(self):
		name = self.cleaned_data['name']
		self.cleaned_data['name'] = name.title()
		# words = [w.capitalize() for w in name.split()]
		# return ' '.join(words)
		return self.cleaned_data['name']

	# Retorno depois que validou o formulario
	def clean(self):
		self.cleaned_data = super().clean()

		if not self.cleaned_data.get('email') and not self.cleaned_data.get('phone'):
			raise ValidationError('Informe email ou telefone.')
		return self.cleaned_data