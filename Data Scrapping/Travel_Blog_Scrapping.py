from selenium import webdriver
from selenium.webdriver.common.by import By
import time 
import pandas as pd
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import os
import csv

def count_words(paragraph):
    words = paragraph.split()

    # Count the total number of words
    total_words = len(words)

    return total_words

    
option = webdriver.EdgeOptions()
user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.150 Safari/537.36"
option.add_argument(f"user-agent={user_agent}")
option.add_argument("start-maximized")
option.add_argument("--disable-blink-features=AutomationControlled")
driver = webdriver.Edge(options=option)
topic = "travel"
pages = ['https://www.nomadicmatt.com/travel-blog/','https://www.nomadicmatt.com/travel-blog/page/2/']


try:
    # Find the "Show more" button
    links = []
    links_with_Topic = []
    for page in pages:
        driver.get(page)
        time.sleep(5)
        div_elements = driver.find_elements(By.CLASS_NAME, "entry-image-link")
        

        # Extract links from each div
        Topic = "Travel"
        for div in div_elements:
            link = div.get_attribute("href")
            links.append(link)
    print("Count = ",len(links),links)
    for link in links:
        driver.get(link)
        time.sleep(5)
        divs = driver.find_elements(By.CLASS_NAME,"content")
        text = ""
        # Iterate through the paragraphs and print their text
        for div in divs:
            text = text + div.text
            wordCount = count_words(text)
            print("Link = ",link," Text = ",text , "Length = ",wordCount)

            links_with_Topic.append((Topic, wordCount,text))


    with open('TravelData.csv', 'w', newline='', encoding='utf-8') as csvfile:
        fieldnames = ['Topic','Word Count','Paragraph']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    
        writer.writeheader()
        for Topic ,WordCount, Text in links_with_Topic:
            writer.writerow({'Topic': Topic, 'Word Count': WordCount,'Paragraph':Text})

    print("Finished")
except Exception as e:
    print("Error = ",e)
    
time.sleep(100)


