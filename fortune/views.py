from django.shortcuts import render
from .models import Fortune
import random

def message_maker_y(year):
    num1 = random.randint(1, 10)
    year = int(year) + num1
    while year > 12:
        year -= 11
    fortune = Fortune.objects.get(ynumber=year)
    messagey = fortune.messages2
    return messagey

def message_maker(month, day):
    if (month == '1' and int(day) <= 19) or (month == '12' and int(day) >= 22):
        number = 1
       #seiza = yagi
    elif (month == '1' and int(day) >= 20) or (month == '2' and int(day) <= 18):
        number = 2
        #seiza = mizugame
    elif (month == '2' and int(day) >= 19) or (month == '3' and int(day) <= 20):
        number = 3
        #seiza = uo
    elif (month == '3' and int(day) >= 21) or (month == '4' and int(day) <= 19):
        number = 4
        #seiza = ohitsuji
    elif (month == '4' and int(day) >= 20) or (month == '5' and int(day) <= 20):
        number = 5
        #seiza = oushi
    elif (month == '5' and int(day) >= 21) or (month == '6' and int(day) <= 21):
        number = 6
        #seiza = futago
    elif (month == '6' and int(day) >= 22) or (month == '7' and int(day) <= 22):
        number = 7
        #seiza = kani
    elif (month == '7' and int(day) >= 23) or (month == '8' and int(day) <= 22):
        number = 8
        #seiza = shishi
    elif (month == '8' and int(day) >= 23) or (month == '9' and int(day) <= 22):
        number = 9
        #seiza = otome
    elif (month == '9' and int(day) >= 23) or (month == '10' and int(day) <= 23):
        number = 10
        #seiza = tenbin
    elif (month == '10' and int(day) >= 24) or (month == '11' and int(day) <= 22):
        number = 11
        #seiza = kani
    elif (month == '11' and int(day) >= 23) or (month == '12' and int(day) <= 21):
        number = 12
        #seiza = ite
    else:
        number = 0
    fortune = Fortune.objects.get(xnumber=number)
    messagex = fortune.messages
    return messagex
# Create your views here.
def fortune_telling(request):
    years = list(range(1900, 2021))
    months = list(range(1, 13))
    days = list(range(1, 32))
    if request.method == 'POST':
        namae_result = "ゲストさん"
        if request.POST.get("onamae"):
            year = request.POST['year']
            month = request.POST['month']
            day = request.POST['day']
            onamae = request.POST["onamae"]
            namae_result = onamae + "さん"
            messagex = message_maker(month, day)
            messagey = message_maker_y(year)
            message = "今日も頑張りましょう！"
            return render(request, 'fortune/result_birth.html', {"days": days, "months": months, 'years': years, "namae_result": namae_result, "message": message, 'messagex': messagex, "messagey": messagey})
        else:
            return render(request, 'fortune/form_birth.html', {'years': years, "months": months, "days": days})
    else:
        return render(request, 'fortune/form_birth.html', {'years': years, "months": months, "days": days})

def fortune_telling_int(request):
    if request.method == 'POST':
        number = request.POST.get("number")
        onamae = request.POST.get("onamae")
        namae_result = onamae + "さん" if onamae else "ゲストさん"

        if number:
            number = int(number)
            if number % 2 == 0:
                if number % 3 == 0:
                    result = "大吉"
                else:
                    result = "中吉"
            else:
                result = "小吉"
            return render(request, 'fortune/result_int.html', {"result": result, "namae_result": namae_result})

    return render(request, 'fortune/form_int.html')
