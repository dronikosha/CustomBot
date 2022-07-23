from django.shortcuts import render, redirect, HttpResponse
import requests
from environs import Env

env = Env()
env.read_env()


# Create your views here.
def index(request):
    # Димин айди стоит
    data = {"access_token": env.str("VK_BOT_KEY"), "user_id": 146653997, "message": "Это тебе написал бот с сайта. Дима лох", "v": "5.131", "random_id": 0}
    if request.method == "POST":
        r = requests.post("https://api.vk.com/method/messages.send", data=data)
        print(r.status_code, r.reason)
        print("test")
    return render(request, 'main/base.html')


def about(request):
    return render(request, 'main/base.html')


def make_request(request):
    return render(request, 'main/base.html')