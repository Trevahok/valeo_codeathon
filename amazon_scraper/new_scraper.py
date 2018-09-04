from bs4 import BeautifulSoup as bs 
from urllib.request import urlopen
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import copied_scraper  as scraper_util
import logging


def get_asins(words):
    web = webdriver.Chrome('/Users/ssvighnesh/chromedriver')  #replace this with an absolute path of a local driver that is downloaded from selenium website
    keywords = '+'.join(words.strip().split())
    web.get('https://www.amazon.in/s?url=search-alias%3Daps&field-keywords=' + keywords)
    page= web.page_source
    soup = bs(page,'lxml')
    things = soup.find_all('li')
    new =[]
    for thing in things:
        if thing.get('data-asin'):
            new.append(thing.get('data-asin'))
    web.close()
    return new

text_to_search = input('enter the term to search for:')
list_of_asins = get_asins(text_to_search)
logging.basicConfig(filename='scraped_data.json',level=logging.INFO,format='%(message)s')

scraper_util.process_handler(list_of_asins)

