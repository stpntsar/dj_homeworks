from django.core.paginator import Paginator
from django.http import HttpResponse
from django.shortcuts import render

DATA = {
    'omlet': {
        'яйца, шт': 2,
        'молоко, л': 0.1,
        'соль, ч.л.': 0.5,
    },
    'pasta': {
        'макароны, г': 0.3,
        'сыр, г': 0.05,
    },
    'buter': {
        'хлеб, ломтик': 1,
        'колбаса, ломтик': 1,
        'сыр, ломтик': 1,
        'помидор, ломтик': 1,
    },
}

def dish_view(request, dish):

    if dish in DATA.keys():
        servings = int(request.GET.get('servings'))
        ingr = {}
        for ingridient in DATA[dish]:
            ingr[ingridient] = DATA[dish][ingridient] * servings
            context = {
                    'recipe': ingr
                }
        return render(request, 'calculator/index.html', context)
