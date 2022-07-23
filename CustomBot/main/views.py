from django.shortcuts import render, redirect, HttpResponse
import requests
from environs import Env

env = Env()
env.read_env()


# Create your views here.
def index(request):
    return render(request, 'main/index.html')


def contact(request):
    # Dima's vk id above
    data = {"access_token": env.str("VK_BOT_KEY"), "user_id": 146653997, "message": "Это тебе написал бот с сайта. Дима лох", "v": "5.131", "random_id": 0}
    if request.method == "POST":
        r = requests.post("https://api.vk.com/method/messages.send", data=data)
        print(r.status_code, r.reason)
    return render(request, 'main/contact.html')