import configparser
import os

# to define the web page that wanted to be crawled
class Requester:

    # input: the state that wanted to be crawled from carlist
    # return: the url of the defined page in form of string
    # defined state: Selangor, Kuala Lumpur, Johor, Penang,
    # Perak, Kedah, Sarawak, and Sabah
    def set_target(self, location:str) -> (str, str):
        setting_file = os.path.join(os.getcwd(), "config.ini")
        parser = configparser.ConfigParser()
        parser.read(setting_file)
        return parser['URL'][location]
