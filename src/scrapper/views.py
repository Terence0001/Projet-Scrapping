from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.http import HttpResponse
from django.conf import settings
from django.contrib.auth.decorators import login_required
from .functions import fn, bdd

from parametres.models.ReleveHistorique import ReleveHistorique

@login_required
def index(request):
    isInterupt = fn.get_isInterupt()
    inAction = fn.get_inAction()
    
    if isInterupt == True and inAction == False:
        isScrapping = "False"
    else:
        isScrapping = "True"
        
    print(isScrapping," _________SCRAPPING_____________")
    print(isInterupt," _________INTERUPT_____________")
    print(inAction," _________ACTION_____________")
    return render(request, 'scrapper_index.html', context={
            "isScrapping": isScrapping,
    })

@login_required
def scrapp(request, projet_id):
    fn.set_isInterupt(False)
    URL = "https://community.o2.co.uk/t5/Discussions-Feedback/bd-p/4"

    last_page_link_number, soup, domain = fn.parseUrl(URL)

    page_request_number = last_page_link_number - 0

    new_threads_number = 0
    while(last_page_link_number >= page_request_number):
        print("last_page_link_number",last_page_link_number)
        print("page_request_number",page_request_number)
        threads = []
        
        # Récupérer les données (threads et posts)
        results = soup.find_all("article", class_="custom-message-tile")
        
        all_threads = fn.getThreads(results, threads)
        
        scrapped_threads = fn.getPosts(domain, all_threads)
        
        if scrapped_threads != None:
            pass
        else:
            fn.set_inAction(False)
            return JsonResponse({"Interupted":True})
        
        # Sauvegarder dans la base de donéne

        nb_new_threads = bdd.savePosts(scrapped_threads, projet_id)
        new_threads_number += nb_new_threads
        
        next_page_url = fn.getNextPageUrl(soup)
        
        last_page_link_number, soup, _ = fn.parseUrl(next_page_url)
        
        page_request_number += 1

    print("the scrapping task is finished")
    # TODO store data into a CSV or relational database
    fn.set_isInterupt(True)
    fn.set_inAction(False)
    return JsonResponse({"finished":True})


@login_required
def interuptScrapp(request):
    fn.set_isInterupt(True)
    fn.set_inAction(False)
    return JsonResponse({"Interupting":True})