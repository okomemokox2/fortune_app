import random
from django.shortcuts import render
from .models import TarotCard

def tarot_shuffle(request):
    cards = TarotCard.objects.all()
    random.shuffle(cards)
    return render(request, 'shuffle.html', {'cards': cards})

def tarot_result(request):
    selected_card_id = random.randint(1, TarotCard.objects.count())
    tarot_number = TarotCard.objects.get(number=selected_card_id)
    selected_card = tarot_number.name
    selected_description = tarot_number.description
    return render(request, 'result.html', {'selected_card': selected_card, "selected_description": selected_description})

from django.shortcuts import render

def tarot(request):
    # タロットの処理を記述する
    return render(request, 'shuffle.html')
