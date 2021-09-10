# the module for scapping web page web elements
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import Firefox
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.firefox.webelement import FirefoxWebElement
import time
import os
import json

class Jsparser:

    # configure the selenium webdriver to using firefox geckodriver
    # then, initiate the selenium web driver
    def initiate_webdriver(self):
        print('[Info] Initiate web driver:')
        options = Options()
        options.headless = True # configure the selenium to initiate without open the webdriver
        geckodriver_path = os.path.join(os.getcwd(), "misc", "geckodriver.exe")
        self.browser = Firefox(executable_path=geckodriver_path,
            options=options)

    # passing the url to selenium webdriver
    # so that the selenium can initiate the web scraping based on the given
    # intial web page
    def get_page(self, url:str):
        print('[Info] Visit {}'.format(url))
        self.browser.get(url)
        time.sleep(5)

    # get the web element of car names and model
    # return a list of car names of max 25 as a list of string
    def get_name(self):
        print('[Info] Get the car names.')
        # element = "//div[@class='grid  grid--full  cf']//div[@class='listing__content  grid__item  soft-half--sides  four-tenths  palm-one-whole relative']//h2[@class='listing__title  epsilon  flush']//a[@class='ellipsize  js-ellipsize-text']"
        # items = self.browser.find_elements_by_xpath(element)
        element = "//script[@type='application/ld+json']"
        item = self.browser.find_element_by_xpath(element).get_attribute('innerHTML') # get the car name using xpath
        attributes = json.loads(item)
        attributes = [name['item']['name'] for name in attributes[0]['itemListElement']]
        if len(attributes) != 0:
            return attributes

    # to get the web element that describe the location of the deal
    # return a list of local location that the car is currently on sale.
    def get_locality(self):
        print('[Info] Get the locality.')
        element = "//script[@type='application/ld+json']"
        item = self.browser.find_element_by_xpath(element).get_attribute('innerHTML')
        attributes = json.loads(item)
        attributes = [name['item']['offers']['seller']['homeLocation']['address']['addressLocality'] for name in attributes[0]['itemListElement']]
        if len(attributes) != 0:
            return attributes

    # get the web element that describe the contact information of the dealer
    # return the web element of contact but not the dealer name and contact number yet
    def get_contact(self):
        print('[Info] Get the dealer contact.')
        element = "//div[@class='grid  grid--full  cf']//div[@class='grid__item  hard  three-tenths  palm-one-half  float--right']//div[@class='visuallyhidden--palm']//div[@class='contact--option  flexbox']//div[@class='flexbox__item']//a"
        item = self.browser.find_elements_by_xpath(element)
        if len(item) != 0:
            return item

    # get the web element where the dealer name is present.
    # some dealer is not putting his or her name, if this happen `None` will be return
    # otherwise, it return a list of dealer name for a particular deal
    # but before get the name must click on the contact button
    # to open the popup window that contain dealer name and contact number
    def get_dealers(self, element:FirefoxWebElement):
        print('[Info] Obtain the dealer info.')
        element.click()
        time.sleep(5)
        dealer_element = "//span[@class='listing__seller-name  js-chat-profile-fullname  c-seller-name  u-text-5  u-margin-bottom-none']"
        dealer_elements = self.browser.find_elements_by_xpath(dealer_element)
        if len(dealer_elements) != 0:
            return [dealer.text for dealer in dealer_elements if dealer.text != ""]
        else:
            return "None"

    # get the web element that descrubes the dealer contact number
    # some deal has more than one contact number
    # thus, this function return a list of contact number
    # if the dealer number is not found, `None` will be return
    def get_dealers_contact(self):
        print('[Info] Obtain the dealer contact.')
        contact_element = "//a[@class='number  weight--semibold  u-text-5  u-text-semibold  u-text-unstyled']"
        contact_elements = self.browser.find_elements_by_xpath(contact_element)
        if len(contact_elements) != 0:
            return [contact.text for contact in contact_elements]
        else:
            return "None"

    # locate the pop up window `x` button
    # then, close the pop up window after the getting the dealer name and contact number
    # must close the pop up window so that next deal contact pop up window can be open.
    def close_window(self):
        print('[Info] Close the pop up window.')
        element = "//div[@class]=flexbox__item  modal__destroy   b-close  weight--light  js-modal-destroy"
        close_button = self.browser.find_element_by_xpath("//div[@class='flexbox__item  modal__destroy   b-close  weight--light  js-modal-destroy']")
        close_button.click()

    # close the selenium webdriver
    # must execute after every crawling session, otherwise
    # it will continue consume computer computation resources.
    def close_driver(self):
        self.browser.quit()

        
