#!/usr/bin/python
import httplib,sys,re
"""
================================================================================
* Name: Rio Atmadja
* Project: ART (Automated Reconnaissance Tool) 
* Program: netcraft.py
* Description: this is class will make query to the netcraft server 
* Course: CSS497
* Date: 06/24/2014 
================================================================================
"""
class netcraft_search():
   
   # this is the default constructor for this class 
   def __init__(self):
      self.url = "" #variable to store the url
      self.userAgent = "Mozilla/5.0 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)"
      self.server = "toolbar.netcraft.com" #the url for the netcraft 
      self.results = "" # store the overall results 
      self.services = [] # array to store all running services 

   # this function will print the banner 
   def banner(self):
      print "[-] Quering Netcraft Server " 
      print "----------------------------"
      return 

   # this function is responsible to make query to the netcraft server 
   def makeQuery(self,url): 
      
      self.banner()
      self.url = url #set the url
      link = httplib.HTTP(self.server)
      link.putrequest( 'GET', "/site_report?url=" + str(self.url) )
      link.putheader('Host', self.server)
      link.putheader('User-agent', self.userAgent) 
      link.endheaders()
      returncode, returnms, headers = link.getreply() 
      self.results = link.getfile().read()

   # this function is responsible to clean up the html query 
   def processQuery(self): 
      
      self.results = re.findall(r'<h2>Background</h2>|<h2>Network</h2>|<h2>Hosting History</h2>|<h2>Security</h2>|<th width=\"13%\">.*.</th>|<td width=\"37%\">.*.</td>|/stats/topsites\?s=.*.|href=\"/netblock\?q.*.|<td>.*.</td>|http://www.spamhaus.org/.*.', self.results) 
      
      for line in self.results:
         line = re.sub(r'<h2>',"\n## ", line)
         line = re.sub(r'</h2>'," ##", line)
         line = re.sub(r'<th width="13%">',"  ",line) 
         line = re.sub(r'</th>',"",line) 
         line = re.sub(r'<td width="37%">',"  ",line) 
         line = re.sub(r'</td>',"",line)
         line = re.sub(r'http://www.spamhaus.org/.*.\">',"  ",line)
         line = re.sub(r'</a>',"", line)
         line = re.sub(r'<a href=\'.*.\'>', "  ", line)
         line = re.sub(r'<span class=\'.*.\'>'," ",line)
         line = re.sub(r'<span class=\".*.\">'," ",line)
         line = re.sub(r'</span>',"", line)
         line = re.sub(r'<img src=\'.*.;', " ", line)
         line = re.sub(r'<td>'," ", line)
         line = re.sub(r'href=".*.">',"  \n", line )
         line = re.sub(r"/stats/topsites\?s=.*.\">", "  ", line)
         print line
   
   # this function is responsible to find the services running on the host server 
   def findServices(self):
      self.results = re.findall(r'<td>.*.<\/td>', self.results) 
      
      for line in self.results:
         line = re.sub(r'<td>', "", line )
         line = re.sub(r'<\/td>', "", line )
         line = re.sub(r'Unix.*.', "", line) 
         line = re.sub(r'Ubuntu.*.', "", line) 
         line = re.sub(r'Phusion.*.',"", line)
         line = re.sub(r'IBM_HTTP_Server.*.', 'IBM_HTTP_Server',line)
         line = re.sub(r'\/', " ",line)
         line = re.sub(r'[0-9]{1,3}.[0-9]{1,3}.[0-9]{1,3}.[0-9]{1,3}',"",line)
         line = re.sub(r'[0-9]{1,2}-[A-Z]{1}[a-z]{2}-[0-9]{4}',"",line)
         line = re.sub(r'unknown',"",line)
         line = re.sub(r'-',"",line)

         if not re.match(r'^\s*$', line):
            self.services.append(line) # append data into the array 

      return self.services # return the array 
