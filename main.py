# -*- coding: utf-8 -*-
"""
Created on Sun Mar 10 20:07:36 2019

@author: wanda
"""
import urllib.request, urllib.parse, urllib.error
from selenium import webdriver
from bs4 import BeautifulSoup
import ssl
import re

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

start_url='https://millercenter.org/the-presidency/presidential-speeches?field_president_target_id[8396]=8396'
key_link='/the-presidency/presidential-speeches/'

html = urllib.request.urlopen(start_url, context=ctx).read()
soup = BeautifulSoup(html, 'html.parser')
tags=soup('a')
links=[]
for tag in tags:
    if tag.get('href',None)!=None:
        s=tag.get('href',None)
        links.append('https://millercenter.org'+s)
speech_links=[]   
for l in links:
    if re.match('https://millercenter.org/the-presidency/presidential-speeches/.+',l):
        speech_links.append(l)
#print(links)       
#print(speech_links)

#get the speed in string
def getSpeech(link):
    driver=webdriver.Chrome()
    driver.get(link)
    elem=driver.find_element_by_class_name("expandable-text-trigger")
    elem.click()
    elems=driver.find_element_by_class_name("transcript-inner")
    text=elems.text
    driver.close()
    return text
                                    
    
speeches=[]
for link in speech_links:
    speeches.append(getSpeech(link))
     
print(speeches[0])