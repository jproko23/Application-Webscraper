#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Aug 10 11:07:17 2020

@author: jphome
"""


from urllib.request import urlopen
from bs4 import BeautifulSoup as soup
from os import environ as env
from twilio.rest import Client

    
#start of code
  
mit_url ='https://mitadmissions.org/apply/firstyear/deadlines-requirements/'

admiss_window = urlopen(mit_url)
page_html = admiss_window.read()
admiss_window.close()

page_soup = soup(page_html, 'html.parser')

p_closed = '<p>The 2020 first-year application is now closed. The 2021 application will be available online in August.</p>'

p_tag = str(page_soup.body.main.div.article.div.p)

if p_tag != p_closed :
  account_sid = env.get('TWILIO_SID')
  auth_token = env.get('TWILIO_AUTH')
  client = Client(account_sid, auth_token)

  message = client.messages.create(
                              body='The MIT Application is now open',
                              from_='+12565810321',
                              to='+17089969412'
                          )

  print(message.sid)
else:
    print('Application is still unavailable')





