from django.shortcuts import render, redirect, HttpResponse, HttpResponseRedirect
from django.urls import reverse_lazy
import requests
from environs import Env
import re
from django.contrib import messages

env = Env()
env.read_env()
# regex = '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'


# Create your views here.
def index(request):
    return render(request, 'main/index.html')


def contact(request):
    # Dima's vk id above
    data = {"access_token": env.str("VK_BOT_KEY"), "user_id": 146653997, "message": "Это тебе написал бот с сайта. Дима лох", "v": "5.131", "random_id": 0}
    if request.method == "POST":
        name = request.POST["name"]
        email = request.POST["email"]
        bot = request.POST["select_bot"]
        message = request.POST["message"]
        if(email and name and bot and message):
            context = {'message': 'Ваше сообщение было отправлено, спасибо за доверие!', 'tag': 'danger'}
            messages.success(request, "Ваше сообщение было отправлено, спасибо за доверие!")
            return HttpResponseRedirect(reverse_lazy('home'))
            messages.success(request, "Ваше сообщение было отправлено, спасибо за доверие!")
            return HttpResponseRedirect(reverse_lazy('contact'))
        else:
            print("Заполните все поля")
            messages.error(request, "Заполните все поля")
            return HttpResponseRedirect(reverse_lazy('contact'))
        print(name, email, bot, message)
        # r = requests.post("https://api.vk.com/method/messages.send", data=data)
        # print(r.status_code, r.reason)
        return redirect("home")
    return render(request, 'main/contact.html')