from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect

# Create your views here.

zodiac_dict = {
    'aries': 'Овен - первый знак зодиака',
    'taurus': 'Телец - первый знак зодиака',
    'gemini': 'Близнецы - третий знак зодиака',
    'cancer': 'Рак - четвертый знак зодиака',
    'leo': 'Лев - пятый знако зодиака',
    'scorpio': 'Скорпион - восьмой знак зодиака',

}

def index(request):


def get_info_about_sign_zodiac(request, sign_zodiac: str):
    description = zodiac_dict.get(sign_zodiac, None)
    if description:
        return HttpResponse(f'<h2>{description}</h2>')
    return HttpResponseNotFound(f"Неизвестный знак зодиака {sign_zodiac}")


def get_info_about_sign_zodiac_by_number(request, sign_zodiac: int):
    zodiacs = list(zodiac_dict)
    if sign_zodiac > len(zodiacs):
        return HttpResponseNotFound(f"Неправильный пороядковый номер {sign_zodiac}")
    name_zodiac = zodiacs[sign_zodiac-1]
    redirect_url = reverse('horoscope_name', args=[name_zodiac])
    return HttpResponseRedirect(f"/horoscope/{name_zodiac-1}")
