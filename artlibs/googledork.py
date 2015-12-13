#!/usr/bin/env python 
import httplib,re,sys,os,time,threading,urllib2

"""
================================================================================
* Name: Rio Atmadja
* Project: ART (Automated Reconnaissance Tool) 
* Program: googledork.py 
* Description: this class will make google dork query to the google server 
* Course: CSS497
* Date: 07/13/2014
================================================================================
"""
class dork:

   # this is the default constructor for this class 
   def __init__(self,word,limit,start):
      self.server = "www.google.com"
      self.userAgent="(Mozilla/5.0 (Windows; U; Windows NT 6.0;en-US; rv:1.9.2) Gecko/20100115 Firefox/3.6"
      self.result = "" # append the current search result 
      self.totalresults = "" # append all the results into one string 
      self.word = word # the search query 
      self.counter = start # page counter 
      self.limit = limit # limit page 
      self.file_extension = "" 
      self.files = [] # array to store the list of files to be downloaded 
      self.headers = { 'User-Agent' : self.userAgent } # given the user agent 
      self.dirs = "./data/" # create data folder in the current directory 

   # this function is responsible to make file dork query to the GOOGLE Server 
   def files_dork(self,exttype): 
      
      google_search = httplib.HTTP(self.server) 
      google_search.putrequest('GET', "/search?num=1000&start=" + str(self.counter)  + "&hl=en&meta=&q=site:" + self.word + "%20ext:" + exttype ) 
      google_search.putheader('Host', self.server)
      google_search.putheader('User-agent', self.userAgent)
      google_search.endheaders()
      returncode, returnmsg, headers = google_search.getreply()
      self.result = google_search.getfile().read()
      self.totalresults += self.result 
      self.file_extension = exttype 

   # this function is responsible to make search dork query to the GOOGLE Server 
   def search_dork(self):     
      google_search = httplib.HTTP(self.server) 
      google_search.putrequest('GET', "/search?num=1000&start=" + str(self.counter)  + "&hl=en&meta=&q=" + self.word ) 
      google_search.putheader('Host', self.server)
      google_search.putheader('User-agent', self.userAgent)
      google_search.endheaders()
      returncode, returnmsg, headers = google_search.getreply()
      self.result = google_search.getfile().read()
      self.totalresults += self.result 

   # this function will behave as the generic browser 
   def genericBrowser(self,url,link):
      query = httplib.HTTP(url)
      query.putrequest('GET', link )
      query.putheader('Host', url)
      query.putheader('User-agent', self.userAgent)
      query.endheaders() 
      returncode, returnmsg, headers = query.getreply() 
      resultquery = query.getfile().read() 
      print resultquery 

   # this function will process the search dork result 
   def process_search_dork(self): 
      while self.counter <= self.limit and self.counter <= 1000:
         self.search_dork()
         time.sleep(5) # sleep for one second   
         self.counter += 100 

   # this function will process the request only one time 
   def process_oneTime(self):
      self.search_dork()
      time.sleep(1) 

   # this function will process all the google dork query 
   def process_filesdork(self,files):
      while self.counter <= self.limit and self.counter <= 1000:
         self.files_dork(files)
         time.sleep(5) # sleep for one second   
         self.counter += 100 
         
   # this function will return the search query 
   def displayFileResults(self):

      #self.files = [] # array to store the results 
      self.totalresults = re.findall(r'<a href=\"\/url.*.<\/a>',self.totalresults) 
      for dork_result in self.totalresults:  
         dork_result = re.sub(r'<div .*.<\/div>',"",dork_result) 
         dork_result = re.sub(r'class=\".*.\"',"",dork_result)
         dork_result = re.sub(r'&.*.',"",dork_result) 
         dork_result = re.sub(r'<a href=',"",dork_result) 
         dork_result = re.sub(r'\"\/url\?q=',"",dork_result)
         self.files.append(dork_result)
   
      if (len(self.files) == 0 ): 
         print "\n[+] Found 0 " + self.file_extension + "files using Google" 
         print "-----------------------------------------------------------\n"
      else: 
         print "\n[+] Searching for " +  self.file_extension +  " files using Google" 
         print "--------------------------------------------------------------------\n"
         # sort the file and print them out 
         for dorkfile in sorted(set(self.files)):
            print "* " ,dorkfile 

   # this function will return the search query 
   def displayDorkResults(self):

      #files = [] # array to store the results 
      self.totalresults = re.findall(r'<a href=\"\/url.*.<\/a>',self.totalresults) 
      for dork_result in self.totalresults:  
         dork_result = re.sub(r'<div .*.<\/div>',"",dork_result) 
         dork_result = re.sub(r'class=\".*.\"',"",dork_result)
         dork_result = re.sub(r'&.*.',"",dork_result) 
         dork_result = re.sub(r'<a href=',"",dork_result) 
         dork_result = re.sub(r'\"\/url\?q=',"",dork_result)
         dork_result = re.sub(r'%3D.*.',"",dork_result)
         dork_result = re.sub(r'%3F.*.',"",dork_result)
         dork_result = re.sub(r'/settings/ads/preferences', "", dork_result)
         self.files.append(dork_result)
   
      if (len(self.files) == 0 ): 
         print "[+] Found 0 dork on Google " 
         print "--------------------------\n" 
      else: 
         print "\n[+] Dorking Google "   
         print "------------------"

         # sort the file and print them out 
         for dorkquery in sorted(set(self.files)):

            # for research purposes you can gather information from pastebin 
            if "pastebin" in dorkquery:
               if "raw.php?i=" in dorkquery:
                  pass
               else:
                  url = "www.pastebin.com"
                  trimurl = os.path.basename(dorkquery)
                  trimurl = "/raw.php?i=" + trimurl 
                  try:
                     self.genericBrowser(url,trimurl)
                  except:
                     print "[X] The link is dead :-< "

            else:
               print dorkquery

   # this function will download the file using a thread 
   def downloadFiles(self,link):
      
      filename = os.path.basename(link)
      if os.path.exists(self.dirs + filename ): # if the file already exists 
         pass # do nothing 

      else: 
         try:
            # request to the server 
            request = urllib2.Request(link, None , self.headers) 
            files = urllib2.urlopen(request) 
            write_file = open(self.dirs + filename, 'w') 
            write_file.write(files.read()) 
            write_file.close() 
            print "[+] Downloading " + link 

         except:
            print "[X] Error Downloading " + link

      
      # this function will process download files using threading library 
   def processDownloadFiles(self):

      if (len(self.files) == 0 ): 
         print "[+] Found 0 files on Google, download cannot be completed " 
         print "---------------------------------------------------------\n" 

      else: 
         print "[+] Downloading files into " + self.dirs 
         print "-----------------------------------------\n"

         if not os.path.exists(self.dirs):
            os.makedirs(self.dirs) # create a directory 
         
         # start mining data 
         for link in sorted(set(self.files)):
            threading.Thread(target=self.downloadFiles, args = (link,)).start() 
#         else:
#            print "[X] Error downloading data " + self.dirs + " already exists "
#            os.removedirs(self.dirs) # remove the exsisting directory 
#            print "[+] removing " + self.dirs 
