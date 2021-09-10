from selenium.webdriver.firefox.webelement import FirefoxWebElement
from jsparser import Jsparser
from requester import Requester
from menu import Menu
from writer import Writer
from selenium.common.exceptions import ElementNotSelectableException
import pandas as pd

# The main program
def main():
    menu = Menu()   # load the menu text description
    state = menu.input() # receives input that is what popular state to crawl
    state_to_crawl = menu.match_state(state) # match the user input key to the desire state


    request = Requester() # get the correct url from the file `config.ini` based on user input index
    url = request.set_target(state_to_crawl) # get the url of the carlist with the selected state
    url = url.split('+1+') # split the original defined url so that it is iterable with the index key later

    jsparser = Jsparser() # calling the wev crawling module
    jsparser.initiate_webdriver() # initiate the selenium webdriver instance

    writer = Writer() # calling the data writing and storing module

    try:
        counter = 0#186 # counter for which page to start to crawl
        while True:


            page_to_crawl = url[0] + str(counter) + url[1]
            jsparser.get_page(page_to_crawl) # passing url to the selenium web driver

            names = jsparser.get_name() # get the car that was put on sale on carlist
            locals = jsparser.get_locality() # get the location the sale is happening
            contacts = jsparser.get_contact() # get the dealer contact element from dom page

            dealer_names = []
            dealer_contacts = []
            for contact in contacts: # loop the contact element to get its child element dealer name and dealer contact
                d_name = jsparser.get_dealers(contact) # get the dealer names
                # print(d_name, type(d_name), len(d_name))
                dealer_names.append(d_name)

                d_contact = jsparser.get_dealers_contact() # get the dealer contact numbers
                dealer_contacts.append(d_contact)

                jsparser.close_window() # close the popup window so next iteration new pop window can be opened
            # print(dealer_names)
            # print(len(names), len(locals), len(dealer_names), len(dealer_contacts))
            data = {
                'cars': names,
                'location': locals,
                'dealer name': dealer_names,
                'dealer contact': dealer_contacts
            } # temporary store the data
            df = pd.DataFrame(data) # format the data as pandas dataframe
            writer.write_data(df) # write or append new data on the device
            # for i in (zip(names, locals, dealer_names, dealer_contacts)):
            #     print(i[0], i[1], i[2], i[3])
            #     print('--')
            # break
            counter += 1
    except: # no more scrapeed element or if there is internet interruption
        print('Done scraping the web page')
        jsparser.close_driver() # close selenium webdriver
    finally:
        jsparser.close_driver() # close selenium webdriver


# Initiate point of the program
# calling the main function
if __name__ == "__main__":
    main()
