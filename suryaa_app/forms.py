from django import forms

class ContactForm(forms.Form):
    name = forms.CharField(max_length=100, required=True)
    phone = forms.CharField(max_length=15, required=True)
    email = forms.EmailField(required=True)
    department = forms.ChoiceField(choices=[
        ('Cardio', 'Cardio'),
        ('Neurology', 'Neurology'),
        ('Gynacology', 'Gynacology'),
    ], required=True)
    message = forms.CharField(widget=forms.Textarea, required=False)