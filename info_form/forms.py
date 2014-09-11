from django import forms
from models import User_input


class User_inputForm(forms.ModelForm):

	class Meta:
		model = User_input
		fields = ('name', 'email', 'services_desired', 'message', 'sample_upload')