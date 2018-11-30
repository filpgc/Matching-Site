from django import forms

GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
)

class RegistrationForm(forms.Form):
	first_name=forms.CharField(label='First Name', max_length=100, widget=forms.TextInput(attrs={
		"placeholder":"First name",
		"pattern":"[[^A-Za-z]{1,150}",
		"name":"firstname",
		"title":"First Names must be between 1 and 150 characters. Only letters are allowed"
	}))
	last_name=forms.CharField(label='Last Name', max_length=100, widget=forms.TextInput(attrs={
		"placeholder":"Last Name",
		"pattern":"[[^A-Za-z]{1,150}",
		"name":"lastname",
		"title":"Last Names must be between 1 and 150 characters. Only letters are allowed"
	}))
	email = forms.EmailField(label='Email Field', widget=forms.TextInput(attrs={
		"placeholder":"Email Field",
		"name":"email field",
	}))
	username = forms.CharField(label='Username', widget=forms.TextInput(attrs={
		"placeholder":"Username",
		"pattern":"[[^A-Za-z0-9]{3,15}",
		"name":"username",
		"title":"Usernames must be between 3 and 15 characters. Only letters and numbers are allowed"
	}))
	password = forms.CharField(label='Password',max_length=32, widget=forms.PasswordInput(attrs={
		"placeholder":"Enter password",
		"pattern":"^(?=.*?[A-Z])(?=.*?[a-z])(?=.*?[0-9])(?=.*?[#?!@$%^&*-]).{8,}$",
		"name":"password",
		"title":"Password must contain at least one number, one uppercase, one lowercase letter and one special character and at least 8 or more characters"
	}))
	repeat_password = forms.CharField(label='Repeat Password',max_length=32, widget=forms.PasswordInput(attrs={
		"placeholder":"Repeat password",
		"name":"repeat_password"
	}))
	gender= forms.CharField(label='What is your gender', widget=forms.RadioSelect(choices=GENDER_CHOICES))