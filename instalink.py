import requests
import re
import urllib, datetime
import time
import os

import json
def instalink(link, name):

    if not os.path.exists(r'D:\insta\{}'.format(name)):
        os.mkdir(r'D:\insta\{}'.format(name))
    print('work')
    templink = "https://www.instagram.com/p/CKG43nNgg-W/"
    tempvid= "https://www.instagram.com/p/CKG5DFTAT7e/"
    testingsidecar="https://www.instagram.com/p/CKd_FWejTr7/"
    test = True
    def test():
        while test:
            x = re.search("#REIMPLEMENT", link)
            # .* matches anything
            # ^	Starts with
            # $	Ends with


            if x:
                # print("YES! We have a match!")
                test = False
                print("Lien validé")
            else:
                print("nope")

    lien = link + "?__a=1"
    print(lien)
    #HTTP header fields:components of the header section of request and response messages in the Hypertext Transfer Protocol
    # They define the operating parameters of an HTTP transaction.


    req=requests.get(lien, headers = {'User-agent': 'ya boi'})
    print(req.status_code,req.ok)

    #print(req.text)
    #print(req.json())

    data=req.json()['graphql']['shortcode_media']
    #checks vid or album(sidecar)
    is_video=data['is_video']
    is_sidecar=(data['__typename']=='GraphSidecar')
    #print(is_video)
    date = datetime.datetime.now().strftime('t%H_%M_d%d%S')
    date = date.replace(':', '_')
    if is_video:
        shortcode = data['shortcode']
        url=data['video_url']
        #print(date)
        #urllib.request.urlretrieve(url, filename=None, reporthook=None, data=None)¶
        #The third arg (if present): callable that will be called once on establishment of the network connection
        # and once after each block read thereafter.
        urllib.request.urlretrieve(url,'D:\insta\{}\{}.mp4'.format(name, shortcode+date))
        print(url)
    elif is_sidecar:

            #data['edge_sidecar_to_children']['edges'] is a list, index 0 contains the part you  need
            sides=data['edge_sidecar_to_children']['edges']
            #index=sides.index('nodes')
            #print(type(sides))
            #print(sides)
            #print(len(sides))
            #print(index)

            #iterate through the dict which will only contain
            for image in sides:
                node=image['node']
                shortcode = node['shortcode']

                if node['is_video']:
                    url = node['video_url']
                    # print(date)
                    # urllib.request.urlretrieve(url, filename=None, reporthook=None, data=None)¶
                    # The third arg (if present): callable that will be called once on establishment of the network connection
                    # and once after each block read thereafter.
                    urllib.request.urlretrieve(url, r'D:\insta\{}\{}.mp4'.format(name, shortcode + date))
                    time.sleep(2)
                    print(url)
                url=node['display_url']
                urllib.request.urlretrieve(url, r'D:\insta\{}\{}.jpg'.format(name, shortcode + date))
                time.sleep(2)

                print(url)

    else:
            shortcode = data['shortcode']
            url = data['display_url']
            urllib.request.urlretrieve(url, r'D:\insta\{}\{}.jpg'.format(name, shortcode + date))
            print(url)


def main():
    instalink(input(), 'test')

if __name__ == "__main__":
    main()
