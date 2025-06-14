from django import forms

class chefForm(forms.Form):
	prompt = forms.CharField(widget=forms.TextInput(
		attrs={
			'placeholder':'Enter your item....',
			'class':'form-control',
			}
		),
		max_length=1000
	)