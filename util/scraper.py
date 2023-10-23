from bs4 import *
import requests
from urllib.parse import urlparse

class Scraper:
    """ Implements a scraper that scrapes web resources for images
    """
    def __init__(self) -> None:
        self.data = {}

    def reset(self) -> None:
        """ Reset the scraper and delete all found resources
        """
        self.data = {}

    def scrape(self, url: str) -> int:
        """ Scrape a given url for images
        url: The web-url to scrape
        returns: number of found images
        """

        r = requests.get(url)
 
        soup = BeautifulSoup(r.text, 'html.parser')
 
        images = soup.findAll('img')

        links = []

        url_parse = urlparse(url)
        base_url = url_parse.scheme + "://" + url_parse.netloc
        for image in images:
            try:
                # In image tag ,searching for "data-srcset"
                image_link = image["data-srcset"]
                links.append(base_url + image_link)
            except:
                try:
                    # In image tag ,searching for "data-src"
                    image_link = image["data-src"]
                    links.append(base_url + image_link)
                except:
                    try:
                        # In image tag ,searching for "data-fallback-src"
                        image_link = image["data-fallback-src"]
                        links.append(base_url + image_link)
                    except:
                        try:
                            # In image tag ,searching for "src"
                            image_link = image["src"]
                            links.append(base_url + image_link)
                        # if no Source URL found
                        except:
                            pass

        self.data[url] = links
        return len(links)
    
    def get_results(self) -> dict:
        """ Get the found resources as a dictionary containing all image links per base url
        returns: Dictionary where the base urls are keys and lists of image urls values
        """
        return self.data
