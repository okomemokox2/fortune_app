# accounts/views.py
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, '登録が完了しました。')  # 登録完了メッセージを設定
    else:
        form = UserCreationForm()
    return render(request, 'signup.html', {'form': form})
