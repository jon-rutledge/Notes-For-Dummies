#! python3

import webbrowser, sys

#literally opens the browser on desktop to this webpage
#webbrowser.open('https://automatetheboringstuff.com/')

#Example of mapping thing

#module for grabbing info from a webpage
import requests

#basic request to grab a webpage
res = requests.get('https://automatetheboringstuff.com/files/rj.txt')

#will rais exception if issue occurred.  i.e. 404 error
res.raise_for_status()
print(res.status_code)

#print sample of text collected
print(res.text[:500])


#can save webpages with following:
#note we must use the 'wb' or write binary param for these
File = open('TestSaveWebpage.txt', 'wb')
for chunk in res.iter_content(100000):
    File.write(chunk)


################################
# WebScrapping
################################


#Beautiful soup module is used for this

import bs4

#Lets try to grab price info from amazon
#for amazon we have to pass a header arguement

#AMAZON EXAMPLE FAILED.  Used Goleta weather instead


headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36',
}

#webbrowser.open('https://www.amazon.com/Professional-Condenser-Microphone-Streaming-Podcasting/dp/B07QKQJL17?pf_rd_p=b14de56b-0fb5-49c5-891d-0d7a5cc73c0e&pd_rd_wg=Y14x4&pf_rd_r=BDJGGZ9KH21789X72X5Z&ref_=pd_gw_cr_cartx&pd_rd_w=q64PV&pd_rd_r=b71c743c-16df-4d6e-84ed-cd1e9cc6d263')
res = requests.get('https://weather.com/weather/hourbyhour/l/Goleta+CA?canonicalCityId=45e562e4a1cb9d0fd5f81861d01ee5d117807444bfef4872c4c9fcbda75e1fcc', headers = headers)
res.raise_for_status()

soup = bs4.BeautifulSoup(res.text, 'html.parser')
vals = soup.select('html body div#APP div div.layout-berlin div.hourly.section-local-suite.page div.section-page-name main.content.layout-centered region.region.region-main div#main-HourlyForecast-d2067ef5-92a1-4934-944c-b13028e80af9 div section.panel.item1.forecast-hourly div.ls-24-hour-wrap.twc-table-wrap.card.panel div#twc-scrollabe.twc-table-scroller table.twc-table tbody tr.closed td.hidden-cell-sm.description span')
print(vals[0].text.strip())



################################
# Using a browser with Selenium.webdriver
################################

#!!!!!!!!!!!!!!!!!!!!!!!!!!!

#Selenium currently broken with my version of FireFox.
#more research and troublehsooting needed

#!!!!!!!!!!!!!!!!!!!!!!!!!!!


# from selenium import webdriver

# browser = webdriver.Firefox()
# browser.get('https://google.com')