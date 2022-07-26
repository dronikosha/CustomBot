from django.shortcuts import render, redirect, HttpResponse, HttpResponseRedirect
from django.urls import reverse_lazy
import requests
from environs import Env
from django.contrib import messages

env = Env()
env.read_env()
# regex = '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'


# Create your views here.
def index(request):
    return render(request, 'main/index.html')


def contact(request):
    if request.method == "POST":
        name = request.POST["name"]
        email = request.POST["email"]
        bot = request.POST["select_bot"]
        message = request.POST["message"]
        if(email and name and bot and message):
            message = f"Имя: {name}\nСвязь: {email}\nСоц. сеть: {bot}\nЗадание:\n {message}"
            data_nikita = {"access_token": env.str("VK_BOT_KEY"), "user_id": 201252666, "message": message, "v": "5.131", "random_id": 0} # Никита
            data_dima = {"access_token": env.str("VK_BOT_KEY"), "user_id": 146653997, "message": message, "v": "5.131", "random_id": 0} # Дима
            r = requests.post("https://api.vk.com/method/messages.send", data=data_nikita)
            r = requests.post("https://api.vk.com/method/messages.send", data=data_dima)
            print(r.reason)
            messages.success(request, "Ваше сообщение было отправлено, спасибо за доверие!")
            return HttpResponseRedirect(reverse_lazy('home'))
        else:
            messages.error(request, "Заполните все поля")
            return HttpResponseRedirect(reverse_lazy('contact'))
    return render(request, 'main/contact.html')