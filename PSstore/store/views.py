from django.contrib.auth import logout
from django.contrib.auth.views import LoginView
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, TemplateView, CreateView
from .forms import *
from .models import *
from datetime import datetime




class Main(ListView):
    model = ProductModel
    template_name = "store/main.html"

    context_object_name = 'model'

class RegisterUser(CreateView):
    form_class = RegisterUserForm
    template_name = 'store/regist.html'

    def get_context_data(self, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        return dict(list(context.items()))

class Login(LoginView):
    form_class = LoginUserForm
    template_name = 'store/login.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)

        return dict(list(context.items()))
    def get_success_url(self):
        return reverse_lazy('main')


def logout_use(request):
    logout(request)
    return redirect('login')

class Order(CreateView):
    form_class = OrderForm
    template_name = "store/order.html"

    def get(self, request, *args, **kwargs):
        now = datetime.date(datetime.now())
        context = {"now": str(now),
                   "form": OrderForm,
                   }
        print(context)
        print(now)
        return render(request, "store/order.html", context=context)
    def get_success_url(self):
        return reverse_lazy('main')
class AddProduct(CreateView):
    form_class = AddProduktForm
    template_name = 'store/addproduct.html'
    def get_success_url(self):
        return reverse_lazy('main')


def main(request):
    return render( request, "store/base.html" )