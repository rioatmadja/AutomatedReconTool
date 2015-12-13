#!/usr/bin/env python
from shodan import WebAPI
"""
================================================================================
* Name: Rio Atmadja
* Project: ART (Automated Reconnaissance Tool) 
* Program: shodansearhquery.py
* Description: this class will make query to shodan server 
* Course: CSS497
* Date: 06/29/2014 
================================================================================
"""

class shodan_search:

   # this function is the default constructor for this class 
   def __init__(self):
		self.key = "" 
      self.api = WebAPI(self.key) # variable to make API call
      self.target = "" # variable to store the target host

   # this function will display the banner 
   def banner(self):
      print "\n[-] Quering Shodan Server"
      print "--------------------------\n"
      return 

   # make shodan API host call 
   def searchShodan(self,hosts):
      self.banner() # display the banner 
      self.target = hosts # set the host 
      hosts = self.api.host(hosts) # make an api call 
   
      results = [] # store all the results in the array 
      for item in hosts['data']:
         print "IP : ", hosts['ip']
         print "Country: " , hosts['country_name'] 
         print "Latitude and Longitude: " , hosts['latitude'] , "," , hosts['longitude'] 
         print "Port: " , item['port']
         print "Banner: " , item['banner']
         print "\n"
