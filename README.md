# Automated Recon Tool 

- Dependencies 
	* pip install pyPdf 
	* pip install fuzzywuzzy
	* pip install dnspython 
	* pip install shodan

- Output:

**************************************************
* 	          _____ _______   		 *
* 	     /\   |  __ \__   __| 		 *
* 	    /  \  | |__) | | |    		 *
* 	   / /\ \ |  _  /  | |    		 *
* 	  / ____ \| | \ \  | |    		 *
* 	 /_/    \_\_|  \_\ |_|    		 *
* ART (Automated Reconnaissance Tool) 		 *
* By: Rio Atmadja             			 *
* rioatmadja@outlook.com                	 *
**************************************************
Usage: Automated Reconnaissance Tool options
     --domain (domain to search and enumerate)
     --google-dork (make google dork)
     --google-dork --download <dork-command> 
     --vulns (automatically find vulnerabilities) 
     --metadata (automatically extract metadata from pdf,xls,ppt,doc )
     --exploit-db <banner> (search exploits in local database )
     --people <name to search> ( Search people on the Internet) 

Example: art.py --domain www.example.com
         art.py --google-dork site:example.com inurl:admin ext:pdf
         art.py --google-dork --download site:example.com inurl:admin ext:pdf
         art.py --vulns www.example.com 
         art.py --metadata <directory> 
         art.py --exploit-database <banner> 
         art.py --people <name to search> 

 ---------------------------------------------- 
             Google Dork Comand                 
 ---------------------------------------------- 
 1. intitle: <title to search> 
 2. inurl: </dir/ to search>
 3. site:<url> 
 4. filetype:<type of files to search>
 5. ext:< search for file extension>
 6. author: <author of the site>
 7. cache: <view the web cache>
 8. related: <view related sites>
 9. intext: <search message in html body>
 10. link: <view link>


- Example
	* Find Open Carts for Remote File Upload vulnerability. ( https://www.exploit-db.com/ghdb/4148/ ) 
	* Command Invoke: python art.py --google-dork intext:\"Powered By OpenCart\" -site:opencart.com -inurl:\"Powered By OpenCart\" -intitle:\"OpenCart\" -intitle:\"powered by\"  
   * Output: 
		- List of Vulnerable Servers 
[+] Dorking Google 
------------------
http://actlandcare.org.au/iv2dalrrge3dknjq
http://actlandcare.org.au/mjquwmbogi2danrrgi
http://affordableradiators.com/
http://africanbynature.com/index.php
http://alliterationink.com/ocart/index.php
http://allthingsergo.com/ergonomic-desk-accessories
http://artsense.ca/
http://au.urlm.com/www.vcsproducts.com.au
http://barksidebistro.com/index.php
http://bartonccc.edu/admissions/IpokIRL_
http://beachsandscoop.com/index.php
http://bubblefarmsoapco.com/store/index.php
http://bulgarianwinemakers.com/store/
http://catalog-demo.opencarthelp.com/
http://chaiware.org/
http://daddydolls.com/
http://dailytrends.duckdns.org/
http://demo.atchworks.com/oc/origin1/index.php
http://demopavothemes.com/pav_summershop/demo1/
http://dergrosshandler.com/
http://discoverycenter.cc/card-game-classes
http://dnepr-kiev.com/index.php
http://electricalconnection.com/index.php
http://em3ev.com/store/index.php
http://enziumlabs.com/Ensens-mmp-2-activity-detection-kit
http://eventusa.com/pft-store/index.php
http://exmailorder.nl/shop/fishtank5
http://fgpadel.com.br/help/category.php
http://flutterwireless.com/index.php
http://foxtravel.club/free-download-pav-decor-responsive-opencart-theme/
http://geribi.com/index.php
http://gerstnerusa.com/1605-kit
http://globalsys.eu/index.php
http://harnishdesign.net/my-theme/opencart/
http://hollanddried.com/index.php
http://inkwater.com/books/index.php
http://interactiveone.com/1naKIKjBI
http://inxspro.com/
http://isenselabs.com/blogs/index/tag/fraudlabspro
http://lazbakkal.biz/
http://lhtp.com/advertising
http://massmark.com.sg/index.php
http://mauk.cc/webshop/cartesio-shop/mechanics
http://max-secure.com.my/
http://mc.boisestate.edu/news/27524
http://micro-trainsline.com/index.php
http://oc.unitegallery.net/index.php
http://oc2.qualityworks.eu/
http://oceanwalkeruk.com/opencart/index.php
http://opencart.hostjars.com/
http://opencart.magetop.com/opencart-2.0.2.0/
http://opencartguru.com/quick-add-to-cart-by-skumodel-
snip ....
