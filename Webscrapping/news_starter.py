# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
import csv
import re
import requests
from bs4 import BeautifulSoup
import datetime
import time

from datetime import datetime as dt


driver = webdriver.Chrome()
# Go to the page that we want to scrape

#sectors = ['Energy', 'Energy', 'Utilities', 'Financials', 'Information Technology', 
#            'Healthcare', 'Industrials', 'Real Estate']

sectors = ['Energy', 'Energy']

urls = ['oil-gas/', 'renewable-energy/', 'utilities/', 'finance/', 'technology/',
       'health-and-science/', 'industrials/', 'real-estate/']

csv_file = open('Python/news/news.csv', 'w', encoding='utf-8', newline='')
writer = csv.writer(csv_file)

for i in range(len(sectors)):
    
    driver.get("https://www.cnbc.com/" + urls[i])
    print("https://www.cnbc.com/" + urls[i])
    print(sectors[i])
    
    index = True
    # We want to start the first two pages.
    # If everything works, we will change it to while True
    while index:
    	try:
            
    		links = []
    		news = driver.find_elements_by_xpath('//div[@class="Card-titleAndFooter"]')
            
    		for new in news:
    			news_dict = {}
                
    			try:
    				mainTitle = new.find_element_by_xpath('.//a[@class="Card-title"]')
                    
    				title = mainTitle.text
    				link = mainTitle.get_attribute("href")
    				date = re.search("([0-9]{4}\/[0-9]{2}\/[0-9]{2})", link)[0]

    				print(date)
                    
    				if dt.strptime(date, '%Y/%m/%d') < dt.strptime('2019/08/25', '%Y/%m/%d'):
    				    break
                    
    				print('hi2')
                    
                    
    				page = requests.get(link)
    				response = BeautifulSoup(page.text, 'html.parser')

    				authorDiv = response.find(class_="Author-author")
    				author = authorDiv.find(class_="Author-authorName").getText()
    				pointsList = response.find(class_="KeyPoints-list")
    				
    				points = []
                    
    				for point in pointsList.findAll('li'):
                        
    				    points.append(point.getText())
    
    #				driver.execute_script("window.open('"+ link + "', 'new window')")
    #				next_window = driver.window_handles[1]
    #                
    #				driver.switch_to.window(next_window)
    #				time.sleep(10)
    #                
    #				authorDiv = driver.find_elements_by_xpath('//a[@class="Author-authorName"]')
    #				author = authorDiv[0].text
    #				print(author)
    #				authorProfile = authorDiv.get_attribute("href")
                    
    				page.close() 
    #				print(authorProfile)
    #				driver.close()
    #				driver.switch_to.window(main_window)
    #				subdriver.find_element_by_tag_name('body').send_keys(Keys.CONTROL + 'w')
    #                driver.switch_to_window(handle)
    #				subdriver.close()
    #				driver.switch_to_window(main_window)
    			except:
    				continue
                
    			print(title)
    			print(i)
    			news_dict['title'] = title
    			news_dict['link'] = link
    			news_dict['date'] = date[0]
    			news_dict['sector'] = sectors[i]
    			news_dict['author'] = author
    			news_dict['points'] = points
    #			news_dict['authorProfile'] = authorProfile
    #			print(news_dict)
                
    			writer.writerow(news_dict.values())
            

        	# Locate the next button element on the page and then call `button.click()` to click it.
    		if (len(driver.find_elements(By.XPATH, '//LoadMoreButton-loadMore')) > 0):
    			button = driver.find_element_by_xpath('//a[@class="LoadMoreButton-loadMore"]')
    			button.click()
    			time.sleep(2)
    		else:
    			time.sleep(2)
    			continue
            
    		driver.close()
#    	index = False
    	except Exception as e:
    		print(e)
    		driver.close()
    		break
        
    driver.close()