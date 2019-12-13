# -*- coding: utf-8 -*-
#from selenium import webdriver
#from selenium.webdriver.common.by import By
#from selenium.common.exceptions import NoSuchElementException 
import time
import csv
import re
import requests
from bs4 import BeautifulSoup
import os
from datetime import datetime as dt

# Go to the page that we want to scrape

sectors = ['Energy', 'Energy', 'Utilities', 'Financials', 'Information Technology', 
            'Healthcare', 'Industrials', 'Real Estate']

#sectors = ['Financials']

urls = ['oil-gas/', 'renewable-energy/', 'utilities/', 'finance/', 'technology/',
       'health-and-science/', 'industrials/', 'real-estate/']

#urls = ['finance/']

csv_columns = ['length', 'num', 'title', 'link', 'date', 'sector', 'subsector', 'author', 'points']
csv_file = open('/home/sofiawangy/Github/Webscrapping/news.csv', 'w', encoding='utf-8', newline='')
#csv_file = open('news.csv', 'w', encoding='utf-8', newline='')
writer = csv.DictWriter(csv_file, fieldnames=csv_columns)
writer.writeheader()

for i in range(len(sectors)):

    index = True
    page_num = 0
    
    print(sectors[i])

    # We want to start the first two pages.
    # If everything works, we will change it to while True
    while index == True:
    	try:
#            https://www.cnbc.com/finance/?page=10
            
    		link = "https://www.cnbc.com/" + urls[i] + '?page=' + str(page_num)
    		print("page", page_num)
            
    		page_num = page_num + 1
            
    		page = requests.get(link)
    		response = BeautifulSoup(page.text, 'html.parser')

    		news = response.findAll("div", {"class": "Card-titleAndFooter"})
            
    		print(len(news))
            
    		if len(news) == 0:
    			index = False
    			break
            
    		for num, new in enumerate(news, start=0):
    			news_dict = {}
                
    			try:

    				mainTitle = new.find(class_="Card-title")
    				title = mainTitle.getText()
                    
    				print("{}: {}".format(num, title))
                    
    				sublink = mainTitle.get('href')
    				date = re.search("([0-9]{4}\/[0-9]{2}\/[0-9]{2})", sublink)[0]

    				if dt.strptime(date, '%Y/%m/%d') < dt.strptime('2019/10/01', '%Y/%m/%d'):
    				    index = False
    				    break
                    
    				subpage = requests.get(sublink)
    				response = BeautifulSoup(subpage.text, 'html.parser')
                    
    				try:
                    
        				if response.find(class_="Author-author") is not None:
        				    authorDiv = response.find(class_="Author-author")
                            
        				    if authorDiv.find(class_="Author-authorName") is not None:
        				        author = authorDiv.find(class_="Author-authorName").getText()
                                
        				    elif authorDiv.find(class_="Author-authorNameAndSocial") is not None:
        				        author = authorDiv.find(class_="Author-authorNameAndSocial").getText()
                                
        				    else:
        				        author = None
        				        print('author not found')
        				        print(sublink)
        				        continue
                                
        				else:
        				    authorDiv = None
        				    author = None
        				    print('authordiv not found')
        				    print(sublink)
        				    continue
    
        				if response.find(class_="KeyPoints-list") is not None:
        				    pointsList = response.find(class_="KeyPoints-list")
        				elif response.find(class_="RenderKeyPoints-list") is not None:
        				    pointsList = response.find(class_="RenderKeyPoints-list")
        				else:
        				    pointsList = None
        				    print('pointslist not found')
        				    print(sublink)
        				    continue
                            
                        
        				points = []
                        
        				if pointsList == None:
        				    points = None
        				    print('points not found')
        				    print(sublink)
        				    continue
                            
        				else:
        				    for point in pointsList.findAll('li'):
        				        points.append(point.getText())
                                
    				except IOError:
        				
        				print("I/O error") 
        				subpage.close() 
        				time.sleep(5)
        				continue
                        
    				subpage.close() 
    				time.sleep(5)
                    
    				news_dict['length']= len(news)
    				news_dict['num'] = num
    				news_dict['title'] = title
    				news_dict['link'] = link
    				news_dict['date'] = date
    				news_dict['sector'] = sectors[i]
    				news_dict['subsector'] = urls[i]
    				news_dict['author'] = author
    				news_dict['points'] = points

    				writer.writerow(news_dict)
                
    			except IOError:
    				print("I/O error") 
    				page.close()
    				time.sleep(5)
    				continue
            
    	except Exception as e:
    		print(e)
    		page.close()
    		time.sleep(5)
    		continue

    page.close()
    
    

