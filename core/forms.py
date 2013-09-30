#encoding: utf-8

from django import forms
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.core.mail import EmailMultiAlternatives

class ContactForm(forms.Form):

	name = forms.CharField(label=u'Nome')
	email = forms.EmailField(label=u'E-mail')
	message = forms.CharField(label=u'Mensagem',
							  widget=forms.Textarea)

	def send_mail(self):
		subject = u'E-mail de Contato de %s' % self.cleaned_data['name']
		context = {
			'name': self.cleaned_data["name"],
			'email': self.cleaned_data["email"],
			'message': self.cleaned_data["message"],
		}
		message = render_to_string("contact_mail.txt")
		message_html = render_to_string("contact_mail.html")
		msg = EmailMultiAlternatives(subject, message, 
									'luizfabiodacruz@gmail.com',
									['luizfabiodacruz@live.com'])
		msg.attach_alternative(message_html, "text/html")
		msg.send()