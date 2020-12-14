# to extract all properties urls (needed to handle with javascript)
from selenium import webdriver
# to access the html content of a single property url
import requests
# to select parts of an XML or HTML text using CSS or XPath and extract data from it
from parsel import Selector
# to access the html content of a single property url
import requests
# to select parts of an XML or HTML using BeautifulSoup (XPath not supported)
from bs4 import BeautifulSoup
# to use regular expressions
import re
# to build a dictionary form a string
import json

import pandas as pd

import pickle


class ImmoWebScraper:

    def __init__(self):
        # The url of each property that resulted from the search will be stored in the "property_url" list.
        self.properties_urls = []
        self.properties_dicts = []
        self.properties_df = pd.DataFrame(columns=['price', 'type_property', 'subtype_property', 'area',
                                                'num_rooms', 'postal_code', 'garden', 'garden_area',
                                                'terrace', 'terrace_area', 'num_facade', 'building_state',
                                                'equipped_kitchen', 'furnished', 'open_fire',
                                                'land_area'])
    
    def get_properties_df(self) -> pd.DataFrame:
        return self.properties_df.copy(deep=True)
    
    def pickle_properties_df(self) -> None:
        with open('src/scraping/properties_df.pickle', 'wb') as file:
            pickle.dump(self.properties_df, file)
    
    def scrape_properties_urls(self) -> None:
        # We choose to not show the browser GUI to scrape faster
        # and to be able to use this on system with no display
        options = webdriver.firefox.options.Options()
        options.headless = True
        driver = webdriver.Firefox(options=options)

        # Iterate through all result pages (i) and get the url of each of them
        base_url = 'https://www.immoweb.be/en/search/house-and-apartment/for-sale?countries=BE&isALifeAnnuitySale=false&isAnInvestmentProperty=false&isAPublicSale=false&propertySubtypes=BUNGALOW,CHALET,FARMHOUSE,EXCEPTIONAL_PROPERTY,COUNTRY_COTTAGE,CASTLE,TOWN_HOUSE,MANSION,VILLA,MANOR_HOUSE,GROUND_FLOOR,DUPLEX,FLAT_STUDIO,LOFT,KOT,PENTHOUSE,TRIPLEX'
        
        num_pages = 1

        for i in range(1, num_pages+1):
            page_num_suffix = '&page=' + str(i)
            url = base_url + page_num_suffix
            
            # The first thing you’ll want to do with WebDriver is navigate
            # to a link. The normal way to do this is by calling get method:    
            driver.get(url)

            # Selector allows you to select parts of an XML or HTML text using CSS
            # or XPath expressions and extract data from it.
            selector = Selector(text=driver.page_source) 

            # Store the xpath query of houses
            xpath_properties = '//*[@id="main-content"]/li//h2//a/@href'
            
            # Find nodes matching the xpath ``query`` and return the result
            page_properties_url = selector.xpath(xpath_properties).extract()
            
            # There are approximately 30 houses in each page.
            # Add each page url list to houses_url, like in a matrix.
            self.properties_urls.append(page_properties_url)

            # An implicit wait tells WebDriver to poll the DOM for a
            #  certain amount of time when trying to find any element 
            #     (or elements) not immediately available. 
            driver.implicitly_wait(10)

        # Store all houses urls in a csv file
        with open('houses_apartments_urls.csv', 'w') as file:
            for page_url in self.properties_urls:
                for url in page_url:
                    file.write(url+'\n')

        # Flattening of the list of lists of URLs
        self.properties_urls = [url for urls_sublist in self.properties_urls for url in urls_sublist]
        
        driver.close()

    def scrape_all_properties_data(self) -> None:
        self.properties_dicts = [{}]*len(self.properties_urls)
        for i, property_url in enumerate(self.properties_urls):
            property_dict = ImmoWebScraper.scrape_unique_property_data(property_url)
            self.properties_dicts[i] = property_dict
            self.properties_df = self.properties_df.append(property_dict, ignore_index=True)
    
    @staticmethod
    def scrape_unique_property_data(url: str) -> dict:
        # attribute referring to the set of houses data (stored in a dictionary; see below)
        property_dict = ImmoWebScraper.generate_property_dict(url)
        
        # final_property_dict: dictionary containing the extracted features of a particular property
        final_property_dict = {}
        
        # set of attributes collected in the dictionary
        final_property_dict['price'] = ImmoWebScraper.price(property_dict)
        final_property_dict['type_property'] = ImmoWebScraper.type_property(property_dict)
        final_property_dict['subtype_property'] = ImmoWebScraper.subtype_property(property_dict)
        final_property_dict['area'] = ImmoWebScraper.area(property_dict)
        final_property_dict['num_rooms'] = ImmoWebScraper.num_rooms(property_dict)
        final_property_dict['postal_code'] = ImmoWebScraper.postal_code(property_dict)
        final_property_dict['garden'] = ImmoWebScraper.garden(property_dict)
        final_property_dict['garden_area'] = ImmoWebScraper.garden_area(property_dict)
        final_property_dict['terrace'] = ImmoWebScraper.terrace(property_dict)
        final_property_dict['terrace_area'] = ImmoWebScraper.terrace_area(property_dict)
        final_property_dict['num_facade'] = ImmoWebScraper.num_facade(property_dict)
        final_property_dict['building_state'] = ImmoWebScraper.building_state(property_dict)
        final_property_dict['equipped_kitchen'] = ImmoWebScraper.equipped_kitchen(property_dict)
        final_property_dict['furnished'] = ImmoWebScraper.furnished(property_dict)
        final_property_dict['open_fire'] = ImmoWebScraper.open_fire(property_dict)
        final_property_dict['land_area'] = ImmoWebScraper.land_area(property_dict)

        return final_property_dict
    
    @staticmethod
    def generate_property_dict(url: str) -> dict:
        '''
        Define a method that creates the dictionary with attributes as keys and houses' values as values
        '''
        html = requests.get(url).content
        soup = BeautifulSoup(html, 'html.parser')

        try:
            # The relevant info is under a "script" tag in the website
            result_set = soup.find_all('script',attrs={"type" :"text/javascript"})
            
            # Iterate through the "script" tags found and keep the one containing the substring "window.classified"
            # which contains all the relevant info
            for tag in result_set:
                if 'window.classified' in str(tag.string):
                    window_classified = tag
                    #when we've found the right tag we can stop the loop earlier
            
            
            # Access to the string attribute of the tag and remove leading and trailing whitespaces (strip)break
            wcs = window_classified.string
            wcs.strip()
            
            # Keep only the part of the string that will be converted into a dictionary
            wcs = wcs[wcs.find("{"):wcs.rfind("}")+1]
            
            # Convert it into a dictionary through json library
            property_dict = json.loads(wcs)

            return property_dict
        except:
            return None
    
    # Define a method to scrap each property attribute    
    @staticmethod
    def price(property_dict: dict) -> int:
        try:
            return int(property_dict['transaction']['sale']['price'])
        except:
            return None

    @staticmethod
    def type_property(property_dict: dict) -> str:
        try:
            return property_dict['property']['type']
        except:
            return None
    
    @staticmethod
    def subtype_property(property_dict: dict) -> str:
        try:
            return property_dict['property']['subtype']
        except:
            return None
    
    @staticmethod
    def area(property_dict: dict) -> int:
        try:
            return int(property_dict['property']['netHabitableSurface'])
        except:
            return None

    @staticmethod
    def num_rooms(property_dict: dict) -> int:
        try:
            return int(property_dict['property']['bedroomCount'])
        except:
            return None
    
    @staticmethod
    def postal_code(property_dict: dict) -> int:
        try:
            return property_dict['property']['location']['postalCode']
        except:
            return None
    
    @staticmethod
    def garden(property_dict: dict) -> int:
        try:
            if property_dict['property']['hasGarden'] ==  True:
                return 1
            else:
                return 0
        except:
            return None
    
    @staticmethod
    def garden_area(property_dict: dict) -> int:
        try:
            if property_dict['property']['hasGarden'] ==  True:
                return property_dict['property']['gardenSurface']
            else:
                return 0
        except:
            return None
    
    @staticmethod
    def terrace(property_dict: dict) -> int:
        try:
            if property_dict['property']['hasTerrace'] == True:
                return 1
            else:
                return 0
        except:
            return None
    
    @staticmethod
    def terrace_area(property_dict: dict) -> int:
        try:
            if property_dict['property']['hasTerrace'] == True:
                return int(property_dict['property']['terraceSurface'])
            else:
                return 0
        except:
            return None
    
    @staticmethod
    def num_facade(property_dict: dict) -> int:
        try:
            return int(property_dict['property']['building']['facadeCount'])
        except:
            return None
    
    @staticmethod
    def building_state(property_dict: dict) -> str: 
        try:
            return property_dict['property']['building']['condition']
        except:
            return None
    
    @staticmethod
    def equipped_kitchen(property_dict: dict) -> int:
        try: 
            property_dict['property']['kitchen']['type']
            return 1
        except:
            return 0
    
    @staticmethod
    def furnished(property_dict: dict) -> int:
        try:
            if property_dict['transaction']['sale']['isFurnished'] == True:
                return 1
            else:
                return 0
        except:
            return None
    
    @staticmethod    
    def open_fire(property_dict: dict) -> int:
        try:
            fire = property_dict['property']['fireplaceExists']
            if fire == True:
                return 1 
            else:
                return 0                
        except:
            return None
    
    @staticmethod
    def land_area(property_dict: dict) -> int:
        try:
            if property_dict['property']['land'] != None:
                return int(property_dict['property']['land']['surface'])
            else:
                return 0
        except:
            return None


if __name__ == '__main__':
    scraper = ImmoWebScraper()
            
    scraper.scrape_properties_urls()

    scraper.scrape_all_properties_data()

    print(scraper.properties_df)

    # for col in scraper.properties_df.columns:
    #     print(scraper.properties_df[col])

    scraper.pickle_properties_df()