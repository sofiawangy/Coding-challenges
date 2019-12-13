# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException 
import time
import csv
import re
import requests
from bs4 import BeautifulSoup

from datetime import datetime as dt

# Go to the page that we want to scrape

#sectors = ['Energy', 'Energy', 'Utilities', 'Financials', 'Information Technology', 
#            'Healthcare', 'Industrials', 'Real Estate']

sectors = ['Financials']

#urls = ['oil-gas/', 'renewable-energy/', 'utilities/', 'finance/', 'technology/',
#       'health-and-science/', 'industrials/', 'real-estate/']

urls = ['finance/']

csv_columns = ['title', 'link', 'date', 'sector', 'subsector', 'author', 'points']
csv_file = open('Python/news/news.csv', 'w', encoding='utf-8', newline='')
writer = csv.DictWriter(csv_file, fieldnames=csv_columns)
writer.writeheader()

for i in range(len(sectors)):
    
    driver = webdriver.Chrome()
    index = True
    
    print("https://www.cnbc.com/" + urls[i])
    driver.get("https://www.cnbc.com/" + urls[i])

    print(sectors[i])

    # We want to start the first two pages.
    # If everything works, we will change it to while True
    while index == True:
    	try:
#            https://www.cnbc.com/finance/?page=10
    		links = []
    		news = driver.find_elements_by_xpath('//div[@class="Card-titleAndFooter"]')
            
    		for num, new in enumerate(news, start=0):
    			news_dict = {}
                
    			try:

    				mainTitle = new.find_element_by_xpath('.//a[@class="Card-title"]')
    				title = mainTitle.text
                
    				print("{}: {}".format(num, title))
                    
    				link = mainTitle.get_attribute("href")
    				date = re.search("([0-9]{4}\/[0-9]{2}\/[0-9]{2})", link)[0]

    				if dt.strptime(date, '%Y/%m/%d') < dt.strptime('2019/11/23', '%Y/%m/%d'):
    				    index = False
    				    break
                    
                    #incorporate beautiful soup in selenium
                    
    				print(link)
                    
    				page = requests.get(link)
    				response = BeautifulSoup(page.text, 'html.parser')
    				authorDiv = response.find(class_="Author-author")
    				author = authorDiv.find(class_="Author-authorName").getText()
                    
    				if response.find(class_="KeyPoints-list") is not None:
    				    pointsList = response.find(class_="KeyPoints-list")
    				elif response.find(class_="RenderKeyPoints-list") is not None:
    				    pointsList = response.find(class_="RenderKeyPoints-list")
    				else:
    				    pointsList = None
                    
    				points = []
                    
    				if pointsList == None:
    				    points = None
    				else:
    				    for point in pointsList.findAll('li'):
        				    points.append(point.getText())

    				page.close() 
                    
    				news_dict['title'] = title
    				news_dict['link'] = link
    				news_dict['date'] = date
    				news_dict['sector'] = sectors[i]
    				news_dict['subsector'] = urls[i]
    				news_dict['author'] = author
    				news_dict['points'] = points

    				writer.writerow(news_dict)
                
    			except NoSuchElementException:
    				continue
                
    			except IOError:
    				print("I/O error") 

    		print((len(driver.find_elements(By.XPATH, '//LoadMoreButton-loadMore')) > 0))

        	# Locate the next button element on the page and then call `button.click()` to click it.
    		if (len(driver.find_elements(By.XPATH, '//LoadMoreButton-loadMore')) > 0):
    			print('button')
    			button = driver.find_element_by_xpath('//a[@class="LoadMoreButton-loadMore"]')
    			button.click()
    			time.sleep(2)
    		else:
    			time.sleep(2)
    			continue
            
    	except Exception as e:
    		print(e)
    		driver.close()
    		continue

    driver.close()
