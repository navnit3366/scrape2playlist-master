#!/usr/bin/python3
# yt_playlist_creator.py - given a file containing youtube video URLs,
# enters those videos into a youtube playlist.

import time
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from cfg import *

def playlist_from_file(infile):

    browser = webdriver.Firefox()
    browser.get('https://www.youtube.com')
    time.sleep(5)
    
    #selects 'log in'
    sign_in = browser.find_element_by_class_name('yt-uix-button-primary')
    sign_in.click()
    time.sleep(5)

    # Logs in
    email = browser.find_element_by_id('identifierId')
    email.send_keys(EMAIL)
    email_next = browser.find_element_by_id('identifierNext')
    email_next.click()
    time.sleep(5)
    password = browser.find_element_by_name('password')
    password.send_keys(PASSWORD)
    password_next = browser.find_element_by_id('passwordNext')
    password_next.click()
    time.sleep(5)
    
    browser.get(LIST_URL) # playlist url
    time.sleep(5)

    #Loop through vids
    for line in open(infile, 'r'):
        browser.switch_to_default_content() #Return from iframe
        vid_url = 'https://www.youtube.com/watch?v=' + line

        # Loop returns here
        add_video = browser.find_element_by_id('gh-playlist-add-video')
        add_video.click()
        time.sleep(3)

        # 3rd instance?
        iframe_instance = browser.find_elements_by_tag_name('iframe')[2] 
        browser.switch_to_frame(iframe_instance)

        # selects 'url' tab, to submit via url
        submit_via_url = browser.find_element_by_id(':6')
        submit_via_url.click()
        time.sleep(3)

        url_here = browser.find_element_by_id(':l')
        add_button = browser.find_element_by_id('picker:ap:2')

        url_here.send_keys(vid_url)

        time.sleep(2)
        add_button.click()
        try:
            WebDriverWait(browser, 2).until(EC.alert_is_present(),
                    'The video you selected no longer exists. ' + 
                    'The owner may have removed it.')
            alert = browser.switch_to.alert
            alert.accept()
            print('deleted:', line)
            browser.get(LIST_URL) # playlist url
            time.sleep(2)

            continue
        except TimeoutException:
            print('added:', line)
            time.sleep(3)

playlist_from_file(URL_TXT_FILE)
