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
pages = ['https://blog.myfitnesspal.com/ask-dietitian-whats-deal-starvation-mode/','https://blog.myfitnesspal.com/a-beginners-guide-to-running-for-weight-loss/',
         'https://blog.myfitnesspal.com/essential-guide-portion-sizes/','https://blog.myfitnesspal.com/how-to-burn-300-calories/',
         'https://blog.myfitnesspal.com/what-is-90-30-50-method/','https://blog.myfitnesspal.com/how-dillion-lost-100-pounds-myfitnesspal-success-story/',
         'https://blog.myfitnesspal.com/walking-with-weight-tips/', 'https://blog.myfitnesspal.com/the-basics-of-body-recomposition-how-to-lose-fat-gain-muscle-at-the-same-time/',
         'https://blog.myfitnesspal.com/always-hungry-and-tired-here-are-8-potential-reasons-why/','https://blog.myfitnesspal.com/macronutrients-vs-micronutrients-how-are-they-different/',
         'https://blog.myfitnesspal.com/kimchi-reduce-risk-of-obesity-study/', 'https://blog.myfitnesspal.com/things-pro-athletes-know-about-nutrition-and-you-should-too/',
         'https://blog.myfitnesspal.com/5-signs-youre-not-eating-enough-protein/', 'https://blog.myfitnesspal.com/how-working-out-supports-your-immune-system/',
         'https://blog.myfitnesspal.com/8-delicious-ways-to-sneak-extra-protein-into-breakfast/'
         ]


try:
    # Find the "Show more" button
    Topic = "HealthAndFitness"
    
    links = []
    links_with_Topic = []
    for page in pages:
        driver.get(page)
        time.sleep(5)
        div_elements = driver.find_elements(By.CLASS_NAME, "elementor-element-1c638d9")
        text = ""
        for div in div_elements:
            text = text + div.text
            wordCount = count_words(text)
            print(" Text = ",text , "Length = ",wordCount)
            links_with_Topic.append((Topic, wordCount,text))
        
    with open('HealthAndFitnessData.csv', 'w', newline='', encoding='utf-8') as csvfile:
        fieldnames = ['Topic','Word Count','Paragraph']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    
        writer.writeheader()
        for Topic ,WordCount, Text in links_with_Topic:
            writer.writerow({'Topic': Topic, 'Word Count': WordCount,'Paragraph':Text})


        # Extract links from each div
    #     for div in div_elements:
    #         link = div.get_attribute("href")
    #         #links.append(link)
    # print("Count = ",len(links),links)
    # for link in links:
    #     driver.get(link)
    #     time.sleep(5)
    #     divs = driver.find_elements(By.CLASS_NAME,"content")
    #     # Iterate through the paragraphs and print their text
    #     for div in divs:
    #         text = text + div.text
    #         wordCount = count_words(text)
    #         print("Link = ",link," Text = ",text , "Length = ",wordCount)

    #         links_with_Topic.append((Topic, wordCount,text))


    

    print("Finished")
except Exception as e:
    print("Error = ",e)
    
time.sleep(100)


