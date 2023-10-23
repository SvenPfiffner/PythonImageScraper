import util
from typing import List, Callable
from os import path, mkdir
import io
import requests
from PIL import Image

class ImageScraper:
    """ Implements an image scraper that is capable of scraping and storing images
    from web sources
    """

    def __init__(self) -> None:
        self.scraper = util.Scraper()

    def scrape(self, urls: List[str], verbose:bool = False) -> None:
        """ Scrape a list of urls for images
        urls: List of urls to scrape
        verbose: If True, status is printed in the terminal
        """
        self.scraper.reset()
        for url in urls:
            self._get_images(url, verbose)

    def save(self, dir:str, generate_json:bool, processing_func:Callable[..., Image.Image] = None, verbose:bool = False) -> None:
        """ Save the images found by a prior scrape to the given directory
        dir: Directory to save the images in
        generate_json: If True, a json is created that stores the respective image sources
        processing_func: A voluntary processing function that should be applied to each downloaded image prior to saving
        verbose: If True, status is printed in the terminal 
        """

        if not path.isdir(dir):
            raise Exception(f'The directory "{dir}" does not exist')
        
        if not path.isdir(dir + "/imgs"):
            mkdir(dir + "/imgs")

        if generate_json:
            json = util.JSONParser()

        scrape_results = self.scraper.get_results()
        img_idx = 0
        for sources in scrape_results.keys():
            links = scrape_results[sources]
            for link in links:
                try:
                    r = requests.get(link, stream=True)
                    if r.status_code == 200:
                        img = Image.open(io.BytesIO(r.content)).convert("RGB")

                        if processing_func is not None:
                            img = processing_func(img)

                        img.save(dir + f"/imgs/img_{str(img_idx)}.jpg")

                        img_idx += 1

                        if generate_json:
                            json.add(f"img_{str(img_idx)}.jpg", sources)

                except Exception as exc:
                    if verbose:
                        print(f"Error loading image {link}")
                        print(exc)

        if generate_json:
            json.save(dir + "/sources.json")

    def _get_images(self, url: str, verbose:bool = False) -> None:
        num_results = self.scraper.scrape(url)

        if verbose:
            print(f"Retrieved {num_results} images from {url}")

        

