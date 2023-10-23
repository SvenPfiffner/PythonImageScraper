# PythonImageScraper
A lightweight python package for image scraping from web-urls

![python_v.3.11.5](https://img.shields.io/badge/Python-v.3.11.5-green)

## Installation
### From repository
- Save the repository in your project root via ```git clone https://github.com/SvenPfiffner/PythonImageScraper.git```
- Install the required dependencies via ```pip install -r requirements.txt```

### As python package
- Install the package on your machine via ```test```

## Usage
Create an image scraper to scrape a collection of urls for images. Then store the found images in an 'out' directory
```python
from image_scraper import ImageScraper
scraper = ImageScraper()
scraper.scrape(["https://davossail.ch/davosersee.shtml", "https://www.davos.ch", ...])
scraper.save("out", generate_json=False)
```
For further use of images it can be beneficial to keep track of the image sources after scraping. This is especially useful in cases where multiple urls were scraped.
To store the sources along with the images the ```generate_json``` flag can be set to ```True```
```python
scraper.save("out", generate_json=True)
```
which saves a JSON file in the output directory that contains the source url for each stored image
```json
{
    "date": "2023-10-23 22:11:55.721009",
    "num_images": "2",
    "num_sources": "1",
    "images": [
        {
            "file": "img_1.jpg",
            "source": "https://davossail.ch/davosersee.shtml"
        },
        {
            "file": "img_2.jpg",
            "source": "https://davossail.ch/davosersee.shtml"
        }
    ]
}
```
For some applications, the user might desire to preprocess the retrieved images in some way. This can be achieved by passing a processing function to ```scraper.save()``` that takes a ```PIL``` image as argument and returns a ```PIL``` image.
This function is then applied to each scraped image prior to saving.
```python
# An image processing function that reduces the size of a PIL image
def resize(img: Image.Image):
    img.thumbnail((128, 128), resample=Image.ADAPTIVE)
    return img

scraper.save("out", generate_json=True, processing_func=resize, verbose=False)
```
