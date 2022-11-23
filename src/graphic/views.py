from django.shortcuts import render

# Create your views here.
def graphique(request):
    return render(request, "graphic/index.html")