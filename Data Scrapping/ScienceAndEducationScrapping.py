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
pages = ['https://www.edutopia.org/article/direct-instruction-active-learning',
         'https://www.edutopia.org/article/helping-students-respectfully-disagree',
         'https://www.edutopia.org/video/calibrating-whole-school-best-practices',
         'https://www.edutopia.org/article/using-technology-math-learning',
         'https://www.edutopia.org/article/increasing-student-pariticipation-real-talk-method',
         'https://www.edutopia.org/article/teaching-students-dyscalculia',
         'https://www.edutopia.org/article/encouraging-ai-adoption-schools',
         'https://www.edutopia.org/article/having-students-produce-authentic-pbl-products',
         'https://www.edutopia.org/article/emotional-intelligence-school-community',
         'https://www.edutopia.org/article/education-myths-not-backed-by-research',
         'https://www.edutopia.org/article/how-to-move-from-the-main-idea-to-background-knowledge',
         'https://www.edutopia.org/article/engaging-closure-activities',
         'https://www.edutopia.org/article/designing-late-work-policy-high-school',
         'https://www.edutopia.org/article/quick-ways-to-check-for-understanding',
         'https://www.edutopia.org/article/using-slide-decks-collaborative-learning',
         'https://www.edutopia.org/article/zoom-interviews-historians-high-school-boost-engagement',
         ]


try:
    # Find the "Show more" button
    Topic = "ScienceAndEducation"
    
    links = []
    links_with_Topic = []
    for page in pages:
        driver.get(page)
        time.sleep(5)
        div_elements = driver.find_elements(By.XPATH, "//*[@id='root']/div/main/div/div/div/div[1]/article/div[1]")
        text = ""
        for div in div_elements:
            text = text + div.text
            wordCount = count_words(text)
            print(" Text = ",text , "Length = ",wordCount)
            links_with_Topic.append((Topic, wordCount,text))
        
    with open('ScienceAndEducationData.csv', 'w', newline='', encoding='utf-8') as csvfile:
        fieldnames = ['Topic','Word Count','Paragraph']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    
        writer.writeheader()
        for Topic ,WordCount, Text in links_with_Topic:
            writer.writerow({'Topic': Topic, 'Word Count': WordCount,'Paragraph':Text})

        

    

    print("Finished")
except Exception as e:
    print("Error = ",e)
    
time.sleep(100)


