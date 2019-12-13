# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
import csv
import re
import requests
from bs4 import BeautifulSoup

driver = webdriver.Chrome()
# Go to the page that we want to scrape

driver.get("https://www.cnbc.com/health-and-science/")

csv_file = open('news.csv', 'w', encoding='utf-8', newline='')
writer = csv.writer(csv_file)

index = 1
# We want to start the first two pages.
# If everything works, we will change it to while True
while index <2:
	try:
        
		print("Scraping Page number " + str(index))
		index = index + 1
        
		links = []
		news = driver.find_elements_by_xpath('//div[@class="Card-titleAndFooter"]')
        
		for new in news:
			news_dict = {}
            
			try:
				mainTitle = new.find_element_by_xpath('.//a[@class="Card-title"]')
                
				title = mainTitle.text
				link = mainTitle.get_attribute("href")
				date = re.search("([0-9]{4}\/[0-9]{2}\/[0-9]{2})", link)
                
				page = requests.get(link)
				response = BeautifulSoup(page.text, 'html.parser')
                
#				if response.status_code == 404:
#								pass
#
#				authorDiv = response.find(class_="Author-author")
#				author = authorDiv.find(class_="Author-authorName").getText()
#				print(author)
				response.close() 
                
			except:
				continue
        
			
			news_dict['title'] = title
			news_dict['link'] = link
			news_dict['date'] = date[0]
			news_dict['sector'] = 'Healthcare'
#			news_dict['author'] = author
#			news_dict['authorProfile'] = authorProfile
			print(news_dict)
            
			writer.writerow(news_dict.values())

    	# Locate the next button element on the page and then call `button.click()` to click it.
		button = driver.find_element_by_xpath('//a[@class="LoadMoreButton-loadMore"]')
		button.click()
		time.sleep(2)
        
	except Exception as e:
		print(e)
		driver.close()
		break