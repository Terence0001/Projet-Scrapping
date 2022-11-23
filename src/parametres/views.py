from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.conf import settings
from django.contrib.auth.decorators import login_required

@login_required
def index(request):
    return render(request, 'index.html', {})
