from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout

@login_required
def base(request):
    return render(request,"index.html")

def salir(request):
    logout(request)
    return redirect('/')