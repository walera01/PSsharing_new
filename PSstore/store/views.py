from django.contrib.auth import logout
from django.contrib.auth.views import LoginView
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, TemplateView, CreateView
from .forms import *
from .models import *
from datetime import datetime, timedelta
from .telegrambot import Send

def view_404(request, exception):
    return render(request,"404.html")
class AddGames(CreateView):
    form_class = GamesForm
    template_name = 'store/addgames.html'

class Main(ListView):
    model = ProductModel
    template_name = "store/main.html"
    context_object_name = 'model'

    def get(self, request, *args, **kwargs):
        game = GamesModel.objects.all()
        model = ProductModel.objects.all()
        context = {'game': game,
                   'model': model
                   }
        return render(request, "store/main.html", context=context)


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
    model = OrderModel()
    now = datetime.date(datetime.now())
    tommorow = now + timedelta(1)
    context = {
            "now": str(now),
            "tommorow": str(tommorow)
        }
    if request.method == 'POST':
        if not request.POST.get('calender_end') or request.POST.get('calender_end') >= request.POST.get('calender'):
            if len(request.POST.get('name')) > 2 and len(request.POST.get('tel')) > 7:
                model.name = request.POST.get('name')
                model.number = request.POST.get('tel')
                model.order_date = request.POST.get('calender')
                if request.POST.get('calender_end'):
                    model.order_date_end = request.POST.get('calender_end')
                model.prod = ProductModel.objects.get(id=id)
                in_tegram = f"Имя: {model.name}\n " \
                            f"Номер телефона: {model.number}\n" \
                            f"Дата с: {model.order_date}\n" \
                            f"До: {model.order_date_end}\n" \
                            f"Модель: {model.prod.name}"
                try:
                    Send(in_tegram)
                except Exception as e:
                    print(e, "В телеграм не пошло")
                try:
                    model.save()
                    err = "Вам позвонят в течении 15 минут"
                except:
                    err = "что-то пошло не так"
                context.update({"err": err})
            else:
                err = "Имя должно быть больше 2-х символов, номер телефона должен быть больше 7 символов"
                context.update({"err":err})
        else:
            err = "Введены неправильные даты"
            context.update({"err":err})

    return render(request, "store/order.html", context=context)


class AddProduct(CreateView):
    form_class = AddProduktForm
    template_name = 'store/addproduct.html'
    def get_success_url(self):
        return reverse_lazy('main')


def main(request):
    return render( request, "store/base.html" )