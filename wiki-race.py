import requests
import random
from bs4 import BeautifulSoup
import wikipediaapi
from sentence_transformers import SentenceTransformer

#connect to wikipediaapi
wiki_wiki = wikipediaapi.Wikipedia(
    'WikiBot-Thaingu (https://www.linkedin.com/in/thai-nguyen8549/)',
    'en',
    timeout = 30
    )

start = input("Enter starting page: ")
end = input("Enter ending page: ")
current = start
#get the best matching wikipedia page based on user input
def get_wiki_page(term):
    search = f"https://en.wikipedia.org/w/index.php?search={'+'.join(term.strip().split())}&title=Special:Search&profile=advanced&fulltext=1&ns0=1"
    soup = BeautifulSoup(requests.get(search).content, "html.parser")
    return soup.find("div", class_ = "mw-search-result-heading").a['href'].replace("/wiki/", "").strip()

#get summary of starting topic
wiki_article = 'Python_(programming_language)'
page_py = wiki_wiki.page(wiki_article)
print(page_py.summary[0:60])

#dictionary of links found on the current wikipedia page
links = page_py.links

#list of "bad" prefixes - commonly lead wikpedia pages that dead end your search
pres = ("List of", "History of", "Template:", "Wikipedia:", "Category:", "Portal:", "Talk:", "Template talk:")

print(len(links))

#deletes keys that start with the above prefixes that are "bad"
for key in list(links.keys()):
    if key.startswith(pres):
        del links[key]

print(len(links))


#get summary of ending topic

#get all links from current wikipedia page and their text associated with it
#def get_links():
  #  pass

#rank the similarity





#loop until current page is end page

#while current != end:
 #   pass

