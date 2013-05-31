#!/usr/bin/env python

#imports
import urllib2
from bs4 import BeautifulSoup, SoupStrainer

def main( url, pages=[] ):    
    #get domain from command line
    domain = url
    
    #if we only have a domain, start scanning from there
    if len( pages ) <1:
        pages = [domain]       
   
   #scan pages
    for p in pages:     
        #curl domain and store html in var
        page = curl( p )
         #find all links back to domain
        pages = get_links( domain, page, pages )
    return pages

def curl( page ):
    #create the request
    request = urllib2.Request( page )
    #get out result
    result = urllib2.urlopen( request )
    return result.read()
def get_links( page, page_content, link_list ):
    for link in BeautifulSoup( page_content, parse_only=SoupStrainer('a')):
        #check for domain links        
        if link.has_attr('href') and len( link['href'].split(page) ) > 1:            
            linker = link['href'].split(page)[1]
            new_page = page+linker
            if new_page not in link_list and '.html' in new_page:                
                link_list.append( new_page )
                print "found: :"+new_page
    return link_list

if __name__ == "__main__":
    main()