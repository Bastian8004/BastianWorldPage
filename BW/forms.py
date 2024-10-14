from django import forms
from BW.models import Services, Qualifications, Contakt, Start, ContaktForm, BlogBW, BlogS, PostBW, PostS
from captcha.fields import CaptchaField

class BlogBWForm(forms.ModelForm):

    class Meta:
        model = BlogBW
        fields = ['tytul','opis','zdjecie', 'lewo', 'prawo']

class PostBWForm(forms.ModelForm):

    class Meta:
        model = PostBW
        fields = ['tytul','opis','zdjecie', 'lewo', 'prawo', 'srodek', 'bez']


class BlogSForm(forms.ModelForm):

    class Meta:
        model = BlogS
        fields = ['tytul','opis','zdjecie', 'lewo', 'prawo']

class PostSForm(forms.ModelForm):

    class Meta:
        model = PostS
        fields = ['tytul','opis','zdjecie', 'lewo', 'prawo', 'srodek', 'bez']


class ServicesForm(forms.ModelForm):

    class Meta:
        model = Services
        fields = ['title', 'description', 'photo', 'left', 'right']


class QualForm(forms.ModelForm):

    class Meta:
        model = Qualifications
        fields = ['title', 'description', 'photo',  'left', 'right', 'srodek', 'bez']


class ContactForm(forms.ModelForm):
    class Meta:
        model = Contakt
        exclude = ['Nazwa', 'NrTel', 'Email','GitHub', 'LinkedIn', 'Facebook']

class ContactFormForm(forms.ModelForm):
    captcha = CaptchaField()
    class Meta:
        model = ContaktForm
        fields = ['dane', 'temat', 'nrtel', 'email', 'wiadomosc']

        widgets = {
            'dane': forms.TextInput(attrs={'placeholder': 'Imię i nazwisko', 'class': 'email-bt'}),
            'temat': forms.TextInput(attrs={'placeholder': 'Temat (np.: Serwis - naprawa)', 'class': 'email-bt'}),
            'nrtel': forms.TextInput(attrs={'placeholder': 'Numer telefonu', 'class': 'email-bt'}),
            'email': forms.EmailInput(attrs={'placeholder': 'Email', 'class': 'email-bt'}),
            'wiadomosc': forms.Textarea(attrs={'placeholder': 'Wiadomość', 'class': 'massage-bt', 'rows': 5}),
        }


class StartForm(forms.ModelForm):
    class Meta:
        model = Start
        exclude = ['title', 'description']


