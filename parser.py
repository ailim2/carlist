# parser to parse carlist web page
# new version this class not used anymore was replaced by jsparser
# since need to execute javascript on the web page
from bs4 import BeautifulSoup
from requester import Requester
import requests
import json

class Parser:

    # get the dom document using the request library
    # input: the web page URL
    # output: DOM document in the format of string
    def get_dom(self, url:str) -> bytes:
        page = requests.get(url)
        return page.content

    # having the html parser and beautifulsoup to parse the HTML dom
    # input: dom document in the format of bytes
    # output: beautifulsoup object
    def dom_parsing(self, dom:bytes) -> BeautifulSoup:
        soup = BeautifulSoup(dom, "html.parser")
        return soup

    # to parse all the car names from carlist website
    # attribute to crawl: name, telephone, company, and area
    # input: dom beautifulsoup and attrubute to crawl
    # output: list of name
    def get_names(self, dom_soup:BeautifulSoup):
        attributes = dom_soup.find("script", type="application/ld+json")
        attributes = str(attributes).replace("</script>","").replace("<script type=\"application/ld+json\">","")
        attributes = json.loads(attributes)
        return [name['item']['name'] for name in attributes[0]['itemListElement']]

    # to parse all the locality from carlist website
    # attribute to crawl: area
    # input: dom beautifulsoup and attrubute to crawl
    # output: list of name
    def get_locality(self, dom_soup:BeautifulSoup):
        attributes = dom_soup.find("script", type="application/ld+json")
        attributes = str(attributes).replace("</script>","").replace("<script type=\"application/ld+json\">","")
        attributes = json.loads(attributes)
        return [name['item']['offers']['seller']['homeLocation']['address']['addressLocality'] for name in attributes[0]['itemListElement']]

    # to parse all the locality from carlist website
    # attribute to crawl: area
    # input: dom beautifulsoup and attrubute to crawl
    # output: list of name
    def get_(self, dom_soup:BeautifulSoup):
        attributes = dom_soup.find("script", type="application/ld+json")
        attributes = str(attributes).replace("</script>","").replace("<script type=\"application/ld+json\">","")
        attributes = json.loads(attributes)
        return [name['item']['offers']['seller']['homeLocation']['address']['addressLocality'] for name in attributes[0]['itemListElement']]
