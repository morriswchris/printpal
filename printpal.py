#!/usr/bin/env python

'''
    PrintPal
    ---------
    -> Automated Site PDF Creation
    
    PrintPal is an html to pdf CLI utility written in Python. Its purpose is to 
    easily take a domain with one or more urls and bundle each html page into one
    pdf document utilizing wkhtmltopdf <http://code.google.com/p/wkhtmltopdf/>. 
    
    **********************************************************************
    
    Usage
    ------
    
    //create a simple page pdf of a site
    $ python printpal.py -D example.com/index.html

    //create a multi-page pdf of a site
    $ python printpal.py -D example.com -I urls.txt

    //create a pdf with a specified output
    $python printpal.py -D example.com -O ~/Desktop/Sample.pdf
    
    **********************************************************************
    
    Available Commands
    ------------------
    
    -D <--domain>: Domain of website to print.
    -I <--uri-file>: file of uri segments to use with domain ( newline delimited ).
    -O <--output>: Path where the file should be saved to.

    
    **********************************************************************
    
    @Author:    Chris Morris http://github.com/morriswchris
    @Date:      July 24 2013
    @version:   1.0.0
    
    Released under the MIT license
'''



#imports
import os
import sys
import getopt
import csv

#
#   Our Main Program
#
def main(argv):
    #maping table for commands
    map_commands = { 'D': 'domain'
                   , 'I': 'uri-file'
                   , 'O': 'output'
                   }
    #try getting arguments
    try:
        opts, args = getopt.getopt( argv
                                  , "D:I:O: h"
                                  , [ "domain="
                                    , "uri-file="
                                    , "output="
                                    ]
                                  )
    except getopt.GetoptError as err:
        usage(err)   
    
    #take out inputs and create our call based on the params
    options = {}
    for opt, value in opts:
        if opt in ["-h", "help"]:
            usage("")
        key = opt.strip("-")
        #replace short tag with long text equivalent
        if map_commands.get(key, False):
            key = map_commands.get(key)
        #ensure we only set the index once
        if not options.get(key, False):
            options[key] = value
    
    #if we have no options go to usage
    if not options:
        usage( "please set options" )
    pdf(options)

#
#   Create our PDF
#
def pdf(options):
	print options
        
        #ensure we atleast have a domain
	if not options.get('domain',False):
            usage( "please set a domain")
                
        #see if we need to do anything extra
        if 'uri-file' in options:
            #get the uris from the file
            urls = urls_from_file( options.get( 'uri-file' ) )
        
        cmd = "wkhtmltopdf "
        for url in urls:
            cmd += " "+options.get('domain')+"/"+url
        cmd += " "+options.get('output',options.get('domain','')+'.pdf')
	print cmd
        os.system(cmd)
	sys.exit(0)

#
#   Read in uri file for urls. 
#
def urls_from_file( file ):
    reader = csv.reader( open( file ), delimiter='\n' )
    urls = [] 
    for row in reader:
        urls.extend( row );   
    #return our urls from file
    return urls

#
#   Man Page
#
def usage( error_str ):
    usage = ""
    if error_str != "":
        usage += "\nThere was an issue with your command. Please review you statment against our list on commands!:\n"
        usage += "\t*"
        usage += str( error_str ) 
    print usage
    print '''    
    PrintPal
    ---------
    -> Automated Site PDF Creation
    
    PrintPal is an html to pdf CLI utility written in Python. Its purpose is to 
    easily take a domain with one or more urls and bundle each html page into one
    pdf document utilizing wkhtmltopdf <http://code.google.com/p/wkhtmltopdf/>. 
    
    **********************************************************************
    
    Usage
    ------
    
    //create a simple page pdf of a site
    $ python printpal.py -D example.com/index.html

    //create a multi-page pdf of a site
    $ python printpal.py -D example.com -I urls.txt

    //create a pdf with a specified output
    $python printpal.py -D example.com -O ~/Desktop/Sample.pdf
    
    **********************************************************************
    
    Available Commands
    ------------------
    
    -D <--domain>: Domain of website to print.
    -I <--uri-file>: file of uri segments to use with domain ( newline delimited ).
    -O <--output>: Path where the file should be saved to.

    
    **********************************************************************
    
    @Author:    Chris Morris http://github.com/morriswchris
    @Date:      July 24 2013
    @version:   1.0.0
    
    Released under the MIT license 
    
    '''
    sys.exit(0)   
    

#call our main app
main(sys.argv[1:])
