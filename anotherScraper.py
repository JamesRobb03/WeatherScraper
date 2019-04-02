#imports
import urllib2
import time
from bs4 import BeautifulSoup
from selenium import webdriver

#code to get url
def getURL():
    userInput = raw_input("Please enter the postcode: ")

    browser = webdriver.Chrome('C:/Users/Jmbo0/Downloads/chromedriver_win32/chromedriver.exe')
    browser.get('https://www.bbc.co.uk/weather')
    search_elem = browser.find_element_by_id('ls-c-search__input-label')
    search_elem.send_keys(userInput)

    search_elem.submit()
    search_elem.submit()
    time.sleep(0.5)

    page_url= browser.current_url
    browser.quit()
    return page_url


#code that finds weather
#page_url = 'https://www.bbc.co.uk/weather/2642347'
def findWeather(page_url):
    page = urllib2.urlopen(page_url)
    soup = BeautifulSoup(page, 'html.parser')

    text_box = soup.find('div', attrs={'class': 'wr-day__weather-type-description wr-js-day-content-weather-type-description wr-day__content__weather-type-description--opaque'})
    location_box = soup.find('h1', attrs={'class':'wr-c-location__name gel-double-pica'})
    text = text_box.text.strip()

    for tag in location_box.find_all('span'):
        tag.replace_with('')

    location = location_box.text.strip();


    print "The forecast for "+location+" is "+text

url = getURL()
findWeather(url)
