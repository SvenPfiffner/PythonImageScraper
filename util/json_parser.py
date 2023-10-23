import datetime
import json

class JSONParser:
    """ Implements a JSON builder that can generate JSONs containing image sources
    """

    def __init__(self) -> None:
        self.data = {}

    def add(self, name: str, source: str) -> None:
        """ Add an image to the JSON
        name: The image filename
        source: The source url of the image
        """
        self.data[name] = source

    def remove(self, name:str) -> None:
        """ Remove an image from the JSON
        name: Filename of the image to remove
        """
        del self.data[name] 

    def update(self, name:str, source: str) -> None:
        """ Update an entry in the JSON
        name: Filename of the image to update
        source: New source for the filename
        """
        self.data[name] = source

    def as_json(self) -> str:
        """ Retrieve the data of this builder as a string formated as per
        JSON specifications
        returns: JSON data as string
        """

        # Date of json creation in ISO 8601
        json_str = '{ "date": "' + str(datetime.datetime.now()) + '",'
        json_str += '"num_images": "' + str(len(self.data)) + '",'
        json_str += '"num_sources": "' + str(len(set(self.data.values()))) + '",'
        json_str += '"images": ['

        i = 1
        for k, v in self.data.items():
            json_str += '{"file": "' + k + '", "source": "' + v + '"}'
            if i < len(self.data):
                json_str += ","
            i += 1 

        json_str += ']}'
        return json_str
    
    def save(self, dir: str) -> None:
        """ Save the data of this builder in a JSON file
        dir: Path of the JSON file
        """
        with open(dir, "w") as f:
            f.write(self.as_json())
    