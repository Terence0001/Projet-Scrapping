from django.shortcuts import render

# Create your views here.
def nav_bar(request):
    return render(request, "nav_bar/index.html")