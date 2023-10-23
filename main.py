from image_scraper import ImageScraper
from PIL import Image

# An image processing function that reduces the size of a PIL image
def resize(img: Image.Image):
    img.thumbnail((128, 128), resample=Image.ADAPTIVE)
    return img

# Create a new scraper
scraper = ImageScraper()

# Scrape one url
scraper.scrape(["https://davossail.ch/davosersee.shtml"])

# Store the results
scraper.save("out", True, resize, True)



