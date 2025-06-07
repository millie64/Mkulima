from django import forms
from .models import Farmer, Product, Order, Report, Vet, Consultation, AI
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
class SignUpForm(UserCreationForm):
    email = forms.EmailField(required=True)
    role = forms.ChoiceField(choices=[('farmer', 'Farmer'), ('vet', 'Vet'), ('admin', 'Admin'), ('supplier', 'Supplier')])

    class Meta:
        model = User
        fields = ('username', 'email', 'role', 'password1', 'password2')


class FarmerForm(forms.ModelForm):
    class Meta:
        model = Farmer
        fields = '__all__'

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = '__all__'
from .models import Supplier

class SupplierForm(forms.ModelForm):
    class Meta:
        model = Supplier
        fields = '__all__'


class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = '__all__'

class ReportForm(forms.ModelForm):
    class Meta:
        model = Report
        fields = '__all__'

class VetForm(forms.ModelForm):
    class Meta:
        model = Vet
        fields = '__all__'

class ConsultationForm(forms.ModelForm):
    class Meta:
        model = Consultation
        fields = '__all__'

class AIForm(forms.ModelForm):
    class Meta:
        model = AI
        fields = '__all__'
