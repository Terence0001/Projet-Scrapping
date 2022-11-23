import requests
from bs4 import BeautifulSoup
from urllib.parse import urlunparse
from urllib.parse import urlparse
import csv  


from parametres.models.Projet import Projet
from parametres.models.ReleveHistorique import ReleveHistorique
from parametres.models.Thread import Thread
from parametres.models.Commentaire import Commentaire
from parametres.models.SuivisReleve import SuivisReleve

class ScrapFunctions():
    
    def __init__(self, isInterupt = False, inAction = False):
        self._isInterupt = isInterupt
        self._inAction = inAction

    def get_isInterupt(self):
        return self._isInterupt

    def set_isInterupt(self, value):
        self._isInterupt = value
        
    def get_inAction(self):
        return self._inAction

    def set_inAction(self, value):
        self._inAction = value
        
    
    def parseUrl(self, url):
        domain = urlparse(url).netloc
        page = requests.get(url)

        soup = BeautifulSoup(page.content, "html.parser")

        last_page_link_number = self.getLastPageUrl(soup)

        return last_page_link_number, soup, domain
        
    def getDomain(self,url):
        domain = urlparse(url).netloc
        return domain

    def getMessages(self, forum_messages, num_page):
        post_messages = []
        for message in forum_messages:
            author_name = ""
            
            author_avatar = message.find("div", class_="lia-message-author-with-avatar")
            if author_avatar.find("span", class_="anon-user"):
                author_name = author_avatar.find("span", class_="anon-user").get_text()
            else:
                author_name = author_avatar.find("a").get_text()
                
            text = message.find("div", class_="lia-message-body-content").get_text()
            print("Page ", num_page, " Author in current page ",author_name)
        
            post_messages.append((author_name, text, num_page))
            
        
        print("----------")
        return post_messages

    def getPostMessages(self, soupObject) :
        next = True
        forum_messages = soupObject.find_all("div", class_="lia-quilt-forum-message")
        
        soup = soupObject
        thread_pages_with_posts = []
        
        num_page_in_thread = 1
        while next:
            next_page_link = None
            next = False
            post_messages = self.getMessages(forum_messages, num_page_in_thread)
            
            thread_pages_with_posts.append(post_messages)
            
            num_page_in_thread+=1
            
            # ENREGISTRER DANS UN CSV ---------------------------------------------
            # with open('Telefonica.csv', 'a', encoding='UTF8') as f:
            #     writer = csv.writer(f)
            #     # write the header
            #     writer.writerow(("Author", "Text", "Numéro de la page"))
                
            #     for message in post_messages:
                
            #         writer.writerow(message)
            #         # f.write("---,".join([message_author, message_text]))
            #         # f.close()
            # ---------------------------------------------
            
            if soup.find("div", class_="lia-paging-pager") != None:
                pager = soup.find("div", class_="lia-paging-pager")
                if pager.find("li", class_="lia-paging-page-next") != None:
                    pagination = pager.find("li", class_="lia-paging-page-next")
                    if pagination.find("a") != None:
                        if pagination.find("a") != None and pagination.find("a")["href"].startswith('https://'):
                            next_page_link = pagination.find("a")["href"]

        
            if next_page_link != None:
                soup = self.getSoupObject("", next_page_link)
                forum_messages = soup.find_all("div", class_="lia-quilt-forum-message")

                next = True
        
        return thread_pages_with_posts
            

    def getPosts(self, domain, threads):
        
        # get all post content for each thread
        all_thread_posts = []
        for thread in threads:
            
            
            if(self._isInterupt != True):
                pass
            else:
                self._inAction = False
                return None
            self._inAction = True
            
            thread_title = thread[0]
            thread_url_path = thread[1]
            thread_author = thread[2]
            thread_page_soup_object = self.getSoupObject(domain, thread_url_path)

            thread_pages_with_posts = self.getPostMessages(thread_page_soup_object)
            
            # thread_pages_with_posts => [ [...(),(),()], [...(),(),()], [...(),(),()] ]
            # thread_pages_with_posts => 
            # Est un conteneur avec plusieurs sous-conteneurs pour les pages du thread contenant chacun plusieurs jeux de donnée pour les posts (author_name, text, num_page)
            
            number_of_messages_in_thread = 0
            for post in thread_pages_with_posts:
                number_of_messages_in_thread += len(post)
            
            
            print(f'Number of post extracted for the thread "{thread_title}": {number_of_messages_in_thread}')
            all_thread_posts.append((thread_title, thread_pages_with_posts, thread_author)) # adding tuples with the title of a thread and the array containing all the posts content of a thread
            print("Number of threads scrapped:", len(all_thread_posts))
        
        return all_thread_posts

        


    def getThreads(self, results, threads):
        # get all threads titles and urls
        for thread_title in results:
            first_element = thread_title.find("div") # get first children - the div
            link = first_element.find("a")
            
            
            
            title = link["title"] # get the title and save it 
            url = link["href"] # get the link towards the post of the thread 
            footer = thread_title.find("footer")
            
            footer_author_link = footer.find("strong").find("a")
            print(footer_author_link)

            author = footer_author_link.find("span").get_text()
            threads.append((title, url, author)) 
            
        return threads
            
            # TODO navigate through all the pages showing threads

    def getSoupObject(self, domain, url_path):
        if domain != "":
            thread_url = urlunparse(('https', domain, url_path, "", "", "")) # construct the url to access the posts for each thread

        else:
            thread_url = url_path
        
        page = requests.get(thread_url)
        soup = BeautifulSoup(page.content, "html.parser")

        return soup

    def getPostsFromPage(self, soup, posts_content):
        thread_results = soup.find_all("div", class_="lia-message-body-content") #piege ici

        for page_posts_content in thread_results:
            body_content = page_posts_content.get_text()   
            posts_content.append(body_content)
        return posts_content

    def getLastPageUrl(self, soup):
        last_pagination_button = soup.find("li", class_="lia-paging-page-last")
        last_page_link = last_pagination_button.find("a")
        last_page_link_number = int(last_page_link.get_text())
        return last_page_link_number

    def getNextPageUrl(self, soup):
        # get to next page 
        
        next_page_li = soup.find("li", class_="lia-paging-page-next")
        if next_page_li.find("span", class_="lia-link-disabled") != None: # should not find disabled span link
            return None
        
        next_page_link = soup.find("li", class_="lia-paging-page-next")
        if next_page_link == None:
            return None
        
        next_page_link_component = next_page_link.find("a", class_="lia-link-navigation") # get the navigation link
        if not next_page_link_component:
            return None
        else:
            next_page_url = next_page_link_component["href"] # get the url for the next page 
        return next_page_url
    
    
fn = ScrapFunctions()


class BddFunctions():
    
    def savePosts(self, scrapped_threads, projet_id):
        # rel = ReleveHistorique.objects.get(id=1)
        nb_new_threads = 0
        
        EN_COURS = "EN_COURS"
        TERMINE = "TERMINE"
        ANNULE = "ANNULE"

        CHOIX_ETAT = (
            (EN_COURS, "En cours"),
            (TERMINE, "Terminé"),
            (ANNULE, "Annulé"),
        )
        
        projet = Projet().__class__.objects.get(id=projet_id)
        
        releve_historique = ReleveHistorique(projet=projet, etat_rel=False, nb_nouveau_threads=0)
        releve_historique.save()
        
        suivis_releve = SuivisReleve(rel_historique=releve_historique)
        suivis_releve.save()
        
        for thread in scrapped_threads:
            thread_title = thread[0]
            thread_pages_with_posts = thread[1]
            thread_author = thread[2]
            
            
            try:
                existing_thread_object = Thread().__class__.objects.get(titre=thread_title, auteur=thread_author)
            except Thread.DoesNotExist:
                # Si le Thread n'existe pas
                new_thread_object = Thread(rel_historique=releve_historique, titre=thread_title, auteur=thread_author)
                new_thread_object.save()
                
                releve_historique.nb_nouveau_threads += 1
                releve_historique.save()
                
                
            except Thread.MultipleObjectsReturned:
                # Si plusieurs threads ont été retrouvés
                for thread in existing_thread_object:
                    thread.delete()
                    
                new_thread_object = Thread(rel_historique=releve_historique, titre=thread_title, auteur=thread_author)
                new_thread_object.save()
                
                releve_historique.nb_nouveau_threads += 1
                releve_historique.save()
            
            for post_messages in thread_pages_with_posts:
                for message in post_messages:
                    author_name = message[0]
                    text = message[1]
                    num_page = message[2]
                    pass
        
        return nb_new_threads


bdd = BddFunctions()