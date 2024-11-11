from selenium import webdriver
import time
import instalink
from random import randint
import re
import json
from json import JSONDecodeError
import os
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import StaleElementReferenceException

import ast


import requests

# Fill in your details here to be posted to the login form.
payload = {
    'inUserName': 'selenium42',
    'inUserPass': ''
}

# Use 'with' to ensure the session context is closed after use.
with requests.Session() as s:
    p = s.post('https://www.instagram.com/', data=payload)
    # print the html returned or something more intelligent to see if it's a successful login page.
    #print(p.text)

    # An authorised request.
        # etc...

test=True
while test:
    link = input('Link ')
    x = re.search('^https:\/\/www.instagram.com\/.*\/?(hl=[a-z])?$', link)
    name=re.search('.com/(.+)', link)
    # .* matches anything
    # ^	Starts with
    # $	Ends with

    if x:
        # print("YES! We have a match!")
        test = False
        found = name.group(1)
        print("Lien validé")
    else:
        print("nope")

name=found[:len(found)-1]
print('name is ', name)

driver = webdriver.Chrome()


savefile=r'D:\insta\{}'.format(name)
fileloc=savefile + '\\{}'.format(name) + '.txt'
print(fileloc)

match=False or os.path.exists(fileloc)
print(match)

current_url = driver.current_url

if match==False:
    driver.get('https://www.instagram.com/accounts/login/?')
    username = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input[name='username']")))
    password = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input[name='password']")))
    username.clear()
    driver.find_element_by_name("username").send_keys('selenium42')
    password.clear()
    driver.find_element_by_name("password").send_keys('fuckmyself')
    time.sleep(1)
    driver.find_element_by_name("password").send_keys(u'\ue007')
    time.sleep(4)
    WebDriverWait(driver, 15).until(EC.url_changes(current_url))
    driver.get(link)

#  enter: "\ue007" is a  key for enter*
#print('waiting')




#print("we gucci")

#{driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")


# Get scroll height
fulllink=set()

lenOfPage = driver.execute_script("window.scrollTo(0, document.body.scrollHeight);var lenOfPage=document.body.scrollHeight;return lenOfPage;")

while(match==False):
        lastCount = lenOfPage
        time.sleep(3)
        lenOfPage = driver.execute_script("window.scrollTo(0, document.body.scrollHeight);var lenOfPage=document.body.scrollHeight;return lenOfPage;")
        # target all the link elements on the page
        time.sleep(2)
        #wait for what? this sleep could be streamlined, rn it's needed because the elements shift but in the older script i had a specific function dedicated to waiting it out, more efficient
        #look into it
        #o8zor ll ssd l9dima ken tajm
        print('into the scrolling')
        myElem = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.TAG_NAME, 'a')))
        print(myElem)
        time.sleep(1)
        print('2')
        links=driver.find_elements_by_tag_name('a')
        time.sleep(2)
        for link in links:
            post= link.get_attribute('href')
            if '/p/' in post:
                #print(post)
                fulllink.add( post )
                if len(fulllink)>100:
                    print(len(fulllink))
                    match = True
                    break



        if lastCount==lenOfPage:
            match=True

time.sleep(2)

if not os.path.exists(savefile):
        os.mkdir(savefile)
print(fileloc)

if not os.path.exists(fileloc):
    with open(fileloc,'w') as file:
            print('file working innit')
            file.write(str(fulllink))
            file.close()

#name=input('name')
#print(name)
print('testing file'+fileloc)


with open("{}".format(fileloc), "r") as f:
    fulllink = set(ast.literal_eval(f.read()))

print(fulllink)
print(type(fulllink))
print(len(fulllink))
i=0

for link in fulllink:
    i+=1
    try:
        instalink.instalink(link, name)
        time.sleep(randint(2,3))
        #exception ssl.SSLError instead of SSLError

    except (JSONDecodeError) as e:
        print('internet prob hmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmm')
        continue
    print(i)
    if i>20:
        print('yzi 3ad lmao')
        break

print(fulllink)
