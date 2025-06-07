from datetime import datetime
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from .forms import (
    SignUpForm, FarmerForm, ProductForm, OrderForm,
    ReportForm, VetForm, ConsultationForm, AIForm
)

def signup_view(request):
    form = SignUpForm(request.POST or None)
    if form.is_valid():
        user = form.save()
        user.profile.role = form.cleaned_data.get('role')
        user.profile.save()
        login(request, user)
        return redirect('dashboard')
    return render(request, 'signup.html', {'form': form})

def login_view(request):
    form = AuthenticationForm(request, data=request.POST or None)
    if form.is_valid():
        user = form.get_user()
        login(request, user)
        return redirect('dashboard')
    return render(request, 'login.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('login')

def home(request):
    return render(request, 'home.html', {'year': datetime.now().year})

@login_required
def dashboard(request):
    role = request.user.profile.role
    return render(request, 'dashboard.html', {'role': role})

@login_required
def add_farmer(request):
    form = FarmerForm(request.POST or None)
    if form.is_valid():
        form.save()
        messages.success(request, "Farmer added successfully!")
        return redirect('dashboard')
    return render(request, 'form_templates.html', {'form': form, 'title': 'Add Farmer', 'year': datetime.now().year})
@login_required
def add_supplier(request):
    if request.user.profile.role != 'admin':
        return HttpResponseForbidden("Access Denied.")

    form = SupplierForm(request.POST or None)
    if form.is_valid():
        supplier = form.save(commit=False)
        supplier.user = request.user  # admin creating supplier
        supplier.save()
        messages.success(request, "Supplier added successfully!")
        return redirect('dashboard')

    return render(request, 'form_templates.html', {
        'form': form,
        'title': 'Add Supplier',
        'year': datetime.now().year
    })

@login_required
def add_product(request):
    form = ProductForm(request.POST or None)
    if form.is_valid():
        form.save()
        messages.success(request, "Product added successfully!")
        return redirect('dashboard')
    return render(request, 'form_templates.html', {'form': form, 'title': 'Add Product', 'year': datetime.now().year})

@login_required
def add_order(request):
    form = OrderForm(request.POST or None)
    if form.is_valid():
        form.save()
        messages.success(request, "Order added successfully!")
        return redirect('dashboard')
    return render(request, 'form_templates.html', {'form': form, 'title': 'Add Order', 'year': datetime.now().year})

@login_required
def add_report(request):
    form = ReportForm(request.POST or None)
    if form.is_valid():
        form.save()
        messages.success(request, "Report added successfully!")
        return redirect('dashboard')
    return render(request, 'form_templates.html', {'form': form, 'title': 'Add Report', 'year': datetime.now().year})

@login_required
def add_vet(request):
    form = VetForm(request.POST or None)
    if form.is_valid():
        form.save()
        messages.success(request, "Vet added successfully!")
        return redirect('dashboard')
    return render(request, 'form_templates.html', {'form': form, 'title': 'Add Vet', 'year': datetime.now().year})

@login_required
def add_consultation(request):
    form = ConsultationForm(request.POST or None)
    if form.is_valid():
        form.save()
        messages.success(request, "Consultation added successfully!")
        return redirect('dashboard')
    return render(request, 'form_templates.html', {'form': form, 'title': 'Add Consultation','year': datetime.now().year})

@login_required
def add_ai(request):
    form = AIForm(request.POST or None)
    if form.is_valid():
        form.save()
        messages.success(request, "AI Diagnosis added successfully!")
        return redirect('dashboard')
    return render(request, 'form_templates.html', {'form': form, 'title': 'Add AI Diagnosis', 'year': datetime.now().year})
