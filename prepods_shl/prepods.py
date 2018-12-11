import urllib.request
from bs4 import BeautifulSoup
import os
import re
import json
import random

def getpeople():
    url = "https://www.hse.ru/org/persons/?ltr%3D%D0%92%D1%81%D0%B5%3Budept%3D141971113"
    req = urllib.request.Request(url, headers = {"User-Agent":"Mozilla/5.0"})
    with urllib.request.urlopen(req) as r:
        text = r.read().decode('utf-8')
    people = re.findall('<a href="/org/persons/[0-9]*"', text)
    with open ('people.txt', 'w', encoding = 'utf-8') as f:
        json.dump(people, f, indent = 4)
    #return people

def getlinks():
    people_links = []
    with open ("people.txt", 'r', encoding = 'utf-8') as f:
        people = json.load(f)
    for p in people:
        pl = re.sub('<a href="(.*)?"', 'https://www.hse.ru\\1', p)
        people_links.append(pl)
    print(people_links)
    with open ('people_links.txt', 'w', encoding = 'utf-8') as f:
        json.dump(people_links, f, indent = 4)
    #return people_links
        
def getstats():
    with open ('people_links.txt', 'r', encoding = 'utf-8') as f:
        urls = json.load(f)
    for url in urls:
        req = urllib.request.Request(url, headers = {"User-Agent":"Mozilla/5.0"})
        with urllib.request.urlopen(req) as r:
            text = r.read().decode('utf-8')
        soup = BeautifulSoup(text, 'html.parser')
        name = soup.find('h1')
        print(name)
        #with open ('people_names.txt', 'a', encoding = 'utf-8') as f:
            #json.dump(name, f, indent = 4)
    
    
        

    
def main():
    getstats()

if __name__ == '__main__':
    main()
    
    
    
