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

def order(request, id):
    form = OrderForm()
    now = datetime.date(datetime.now())
    context = {"now": str(now) }
    if request.method == 'POST':
        if not request.POST.get('calender-end') or request.POST.get('calender-end')>=request.POST.get('calender'):
            form.name = request.POST.get('name')
            form.number = request.POST.get('tel')
            form.order_date = request.POST.get('calender')
            if request.POST.get('calender-end'):
                form.order_date_end = request.POST.get('calender-end')
            form.prod = ProductModel.objects.get(id=id)
            print(form.name)
            print(form.number)
            print(form.order_date)
            print(form.prod)
            if form.is_valid():
                pass
            form.save()
            err = "Вам позвонят в течении 15 минут"
            # else:
            #     err = "что-то не так"
            context.update({"err": err})
        else:
            err = "Введены неправильные даты"
            context.update({"err":err})

    return render(request, "store/order.html", context=context)

class Order(CreateView):
    form_class = OrderForm
    template_name = "store/order.html"

    def get(self, request, *args, **kwargs):
        now = datetime.date(datetime.now())
        context = {"now": str(now),
                   "form": OrderForm,
                   }

        return render(request, "store/order.html", context=context)

    def post(self, request, *args, **kwargs):
        now = datetime.date(datetime.now())
        print(request.form["calender_end"],request.form["calender"])
        if request.form["calender_end"] < request.form["calender"]:

            err = "Ошибка ввода даты"
            context = {"now": str(now),
                       "form": OrderForm,
                       "err": err,
                       }
            return render(request, "store/order.html", context = context)
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