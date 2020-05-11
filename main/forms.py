from django import forms
from main.models import Master, Reception, UserProfile, ContactsForm, Stock,StockReserv
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.admin import widgets

class ContactsForms(forms.ModelForm):
    message = forms.CharField(widget=forms.Textarea(attrs={'cols': 80, 'rows': 20}))

    class Meta:
        model = ContactsForm
        fields = ('person', 'mail', 'message')

class StockForm(forms.ModelForm):

    class Meta:
        model = StockReserv
        fields = '__all__'


class ReceptionForm(forms.ModelForm):
    class Meta:
        model = Reception
        fields = ('date','time','client_name','client_info','uslugi', 'cost', 'person_id')

    def __init__(self, *args, **kwargs):
        super(ReceptionForm, self).__init__(*args, **kwargs)
        self.fields['time'].widget = forms.HiddenInput()
        self.fields['client_info'].widget = forms.Textarea(attrs={'cols': 60, 'rows': 8})
        self.fields['client_info'].label = 'Ваши пожелания'
        self.fields['uslugi'].widget = forms.HiddenInput();
        self.fields['cost'].widget = forms.HiddenInput();
        # self.fields['uslugi'].label = 'Список услуг'
        self.fields['person_id'].label = ''

class UserCreateForm (UserCreationForm):
    # email = forms.EmailField(required = True)


    class Meta :
        model = User
        fields = ("first_name","last_name","username","email","password1","password2")

    def save(self, commit=True):
        user = super(UserCreateForm, self).save(commit=False)
        user.email = self.cleaned_data["email"]
        if commit:
            user.save()
        return user


class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email')


class ProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ('avatar', 'phone')