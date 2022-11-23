import functions as fn

URL = "https://community.o2.co.uk/t5/Discussions-Feedback/bd-p/4"


last_page_link_number, soup, domain = fn.parseUrl(URL)

page_request_number = last_page_link_number - 2

while(last_page_link_number > page_request_number):
    print("last_page_link_number",last_page_link_number)
    print("page_request_number",page_request_number)
    threads = []
    
    # get all articles
    results = soup.find_all("article", class_="custom-message-tile")
    
    all_threads = fn.getThreads(results, threads)
    
    fn.getPosts(domain, all_threads)
    
    next_page_url = fn.getNextPageUrl(soup)
    
    last_page_link_number, soup, _ = fn.parseUrl(next_page_url)
    
    page_request_number += 1
    
print("the scrapping task is finished")
# TODO store data into a CSV or relational database