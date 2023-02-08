from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound

# Create your views here.

zodiac_dict = {
    'leo': 'Лев - пятый знако зодиака',
    'scorpio': 'Скорпион - восьмой знак зодиака',
    'taurus': 'Овен - первый знак зодиака'
}


def get_info_about_sign_zodiac(request, sign_zodiac: str):
    description = zodiac_dict.get(sign_zodiac, None)
    if description:
        return HttpResponse(description)
    return HttpResponseNotFound(f"Неизвестный знак зодиака {sign_zodiac}")


def get_info_about_sign_zodiac_by_number(request, sign_zodiac: int):
    return HttpResponse(f"This is number {sign_zodiac}")
