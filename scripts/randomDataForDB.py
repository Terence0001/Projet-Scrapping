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

def randomRelH():
    #f = open("releveHistorique.json", "a")
    f = open("../src/parametres/fixtures/releveHistorique.json", "a")
    f.write("[")
    for i in range(1,21):
        f.write(str({
            "pk": i,
            "model": "parametres.releveHistorique",
            "fields": {
                "date_rel": random_date(
                    datetime.strptime('1/1/2022', '%m/%d/%Y'),
                    datetime.strptime('12/12/2022', '%m/%d/%Y')
                    ).strftime("%Y-%m-%d"),
                "etat_rel": random.randint(0, 1),
                "projet_id": random.randint(1, 3)}
            })+str(",\n"))
    f.write("]")
    f.close()


def randomThread():
    f = open("../src/parametres/fixtures/thread.json", "a")
    f.write("[")
    for i in range(1,21):
        f.write(str({
            "pk": i,
            "model": "parametres.thread",
            "fields": {
                "titre": "Titre Thread",
                "auteur": "gklsehjf",
                "rel_historique_id": random.randint(1, 3)}
            })+str(",\n"))
    f.write("]")
    f.close()

#randomRelH()
randomThread()
print('fini')