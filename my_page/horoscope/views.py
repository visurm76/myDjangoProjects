from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound


# Create your views here.


def get_info_about_sign_zodiac(request, sign_zodiac):
    if sign_zodiac == 'leo':
        return HttpResponse('Знак зодиака Лев')
    elif sign_zodiac == 'scorpio':
        return HttpResponse('Знак зодиака Скорпион')
    return HttpResponseNotFound(f"Неизвестный знак зодиака {sign_zodiac}")
