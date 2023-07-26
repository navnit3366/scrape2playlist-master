#! python3
# dg_yt_scraper.py - scrapes dg's 6um for posted youtube videos,
# then writes those youtube ids to a file for later manipulation.
# saved file is named after thread title.

# TODO: Add last post# so bot doesn't have to re-scrape?
# TODO: Detect thread length (post_num) automatically

import requests, bs4
from bs4 import BeautifulSoup
from cfg import *

#increment by 26 (initially loads 20 posts)
loaded = 0

vid_ids = []
vid_names = {}

def new_url(SCRAPE_URL, loaded):
    """
    Creates a new url by appending loaded, an int, to the 
    original url. loaded denotes how far the bot has read 
    through the thread (0 by default).

    Proceeds to load the page and check if the link is valid.
    loaded is then incremented by 26, ensuring that the next 
    load will be unread content
    """
    new_url = str(SCRAPE_URL) + str(loaded)
    thread_obj = requests.get(new_url)
    soup = BeautifulSoup(thread_obj.text, "html.parser")

    try:
        thread_obj.raise_for_status()
        print('Loaded', SCRAPE_URL + str(loaded))
    except requests.exceptions.RequestException as e:
        print('An error occurred.')
        exit()

    elements = soup.select('[data-youtube-id]')
    if len(elements) > 0:
        print('Videos found:')
        for element in elements:
            vid_ids.append(element.get('data-youtube-id'))
            #vid_names[element.get('data-youtube-id')] \
                    #= element.get('data-youtube-title')
            print(element.get('data-youtube-title'), '(' \
                    + element.get('data-youtube-id') + ')')
    else:
        print('No videos found!')
        
print('Loading Thread...')
thread_obj = requests.get(SCRAPE_URL)
soup = BeautifulSoup(thread_obj.text, "lxml")

print(soup.title.string)
print()

while loaded < THREAD_LEN + 25:
    new_url(SCRAPE_URL, loaded)    
    print()
    loaded += 26

print('Scraping complete.')

title = soup.title.string
title_list = title.split(' ')
title_underscore = '_'.join(title[:-4])

f = open(title_underscore + '.txt', 'w')
vid_str = '\n'.join(vid_ids)
f.write(vid_str)
f.close()
