from django.shortcuts import render
#from functions import randomData
from parametres.models.ReleveHistorique import ReleveHistorique
from parametres.models.Thread import Thread
from django.db import connection

# Create your views here.
def pageHistorique(request):

    #print("-----------------------------------------------")
    #print(ReleveHistorique.objects.all().values())
    # res = Thread.objects.raw('''SELECT COUNT(titre),
    #                             FROM parametres_thread,
    #                             GROUP BY rel_historique_id;''')
    #cursor  = connection.cursor()
    #cursor.execute(''' SELECT *
    #                   FROM parametres_thread; ''')

    #print("-----------------------------------------------")
    #resL = randomData()
    return render(request, "page_historique/index.html", {'data': ReleveHistorique.objects.all().values()})


# ----------------------------------------------------------------------------------------------------------------------
import random
import time
from random import randrange
from datetime import timedelta
from datetime import datetime

def random_date(start, end):
    """
    This function will return a random datetime between two datetime
    objects.
    """
    delta = end - start
    int_delta = (delta.days * 24 * 60 * 60) + delta.seconds
    random_second = randrange(int_delta)
    return start + timedelta(seconds=random_second)

def randomData():
    resL = []
    for i in range(0, 20):
        resL.append({
            "date": random_date(
                datetime.strptime('1/1/2022', '%m/%d/%Y'),
                datetime.strptime('12/12/2022', '%m/%d/%Y')
            ).strftime("%d/%m/%Y"),
            "nbTh" : random.randint(1, 100),
            "status": random.randint(0, 1)
        })
    return resL