from django import forms


class UserForm(forms.Form):
    name = forms.CharField(label="Ім'я клієнта")
    age = forms.IntegerField(label="Вік",required=False)
    basket = forms.BooleanField(label="Покласти товар в кошик", label_suffix=" ?", required=False)