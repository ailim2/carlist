import configparser
import os

# running this file to create the configration file for the syste
# running this file only when the "config.ini" was not found

config = configparser.ConfigParser()

config['URL'] = {
    "MALAYSIA": "https://www.carlist.my/cars-for-sale/malaysia?page_number=1&page_size=25",
    "SELANGOR": "https://www.carlist.my/cars-for-sale/malaysia_selangor?page_number=1&page_size=25",
    "KUALA_LUMPUR": "https://www.carlist.my/cars-for-sale/malaysia_kuala-lumpur?page_number=1&page_size=25",
    "PENANG": "https://www.carlist.my/cars-for-sale/malaysia_penang?page_number=1&page_size=25",
    "PERAK": "https://www.carlist.my/cars-for-sale/malaysia_perak?page_number=1&page_size=25",
    "KEDAH": "https://www.carlist.my/cars-for-sale/malaysia_kedah?page_number=1&page_size=25",
    "SARAWAK": "https://www.carlist.my/cars-for-sale/malaysia_sarawak?page_number=1&page_size=25",
    "SABAH": "https://www.carlist.my/cars-for-sale/malaysia_sabah?page_number=1&page_size=25",
    "JOHOR": "https://www.carlist.my/cars-for-sale/malaysia_johor?page_number=1&page_size=25"
}

config['FORMAT'] = {
    "excel": "excel",
    "csv": "csv"
}

setting_file = os.path.join(os.getcwd(), "config.ini")
with open(setting_file, "w") as configFile:
    config.write(configFile)
