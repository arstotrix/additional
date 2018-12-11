import urllib.request
from bs4 import BeautifulSoup
import os
import re
import json
import random

def getpeople():
    url = "https://ling.hse.ru/persons"
    req = urllib.request.Request(url, headers = {"User-Agent":"Mozilla/5.0"})
    with urllib.request.urlopen(req) as r:
        text = r.read().decode('utf-8')
    people = re.findall('href="//www.hse.ru/org/persons/[0-9]+"', text)
    staff = re.findall('href="//www.hse.ru/staff/[a-zA-Z]+"', text)
    #print(staff)
    people += staff
    with open('people.txt', 'w', encoding = 'utf-8') as f:
        json.dump(people, f, indent = 4)
    #with open ('staff.txt', 'w', encoding = 'utf-8') as f:
        #json.dump(staff, f, indent = 4)
    #return people

def getlinks():
    people_links = []
    with open("people.txt", 'r', encoding = 'utf-8') as f:
        people = json.load(f)
    for p in people:
        pl = re.sub('href="(.*)?\"', 'https:\\1/', p)
        if pl not in people_links:
            people_links.append(pl)
    #print(people_links)
    with open('people_links.txt', 'w', encoding = 'utf-8') as f:
        json.dump(people_links, f, indent = 4)
    #return people_links
        
def getstats():
    names = []
    interests = {}
    with open('people_links.txt', 'r', encoding = 'utf-8') as f:
        urls = json.load(f)
    for url in urls:
        name_interests = []
        req = urllib.request.Request(url, headers = {"User-Agent":"Mozilla/5.0"})
        with urllib.request.urlopen(req) as r:
            text = r.read().decode('utf-8')
        soup = BeautifulSoup(text, 'html.parser')
        name = str(soup.find('h1'))
        name = re.sub('<h1(.*)?>(.*)?</h1>', '\\2' ,name)
        #print(name)
        intrst = str(soup.find('div', {"class":"b-person-data b-person-data__tags"}))
        if intrst != None and len(intrst) != 0:
            intrst = intrst.split(">")
            for i in intrst:
                if not i.startswith('<') and not i.startswith('Профессиональные'):
                    name_interests.append(i.strip('</a'))
            name_interests = name_interests[:-1]
            #for i in intrst:
                #print(i)
        #print(name_interests)
        names.append(name)
        interests[name] = name_interests
        with open ('names.txt', 'w', encoding = 'utf-8') as f:
            json.dump(names, f, indent = 4)
        with open ('interests.txt', 'w', encoding = 'utf-8') as f:
            json.dump(interests, f, indent = 4)
    return names, interests
        
def playgame(names, interests):
    with open ('names.txt', 'w', encoding = 'utf-8') as f:
        names = json.load(f)
    with open ('interests.txt', 'w', encoding = 'utf-8') as f:
        interests = json.load(f)
    name = random.choice(names)
    print(name, interests[name])
        
    
def main():
    getstats()
    #playgame(a, b)

if __name__ == '__main__':
    main()
