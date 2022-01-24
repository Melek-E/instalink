from selenium import webdriver
import time
import instalink
from random import randint
import re
from json import JSONDecodeError
import os
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait



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



driver.get('https://www.instagram.com/accounts/login/?')
current_url = driver.current_url

username = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input[name='username']")))
password = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input[name='password']")))
username.clear()
driver.find_element_by_name("username").send_keys(input('username'))
password.clear()
driver.find_element_by_name("password").send_keys(input('password'))
time.sleep(1)
driver.find_element_by_name("password").send_keys(u'\ue007')

WebDriverWait(driver, 15).until(EC.url_changes(current_url))
driver.get(link)
#  enter: "\ue007" is a  key for enter*
#print('waiting')




#print("we gucci")

#{driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")


# Get scroll height
fulllink=set()
lenOfPage = driver.execute_script("window.scrollTo(0, document.body.scrollHeight);var lenOfPage=document.body.scrollHeight;return lenOfPage;")
match=False
while(match==False):
        lastCount = lenOfPage
        time.sleep(3)
        lenOfPage = driver.execute_script("window.scrollTo(0, document.body.scrollHeight);var lenOfPage=document.body.scrollHeight;return lenOfPage;")
        # target all the link elements on the page
        time.sleep(4)
        #wait for what? this sleep could be streamlined, rn it's needed because the elements shift but in the older script i had a specific function dedicated to waiting it out, more efficient
        #look into it
        #o8zor ll ssd l9dima ken tajm
        myElem = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.TAG_NAME, 'a')))
        links=driver.find_elements_by_tag_name('a')

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
time.sleep(4)

#name=input('name')
#print(name)

print(fulllink)
print(len(fulllink))
i=0
if not os.path.exists(r'D:\insta\{}'.format(name)):
        os.mkdir(r'D:\insta\{}'.format(name))
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
    if i>101:
        print('yzi 3ad lmao')
        break


