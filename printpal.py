#!/usr/bin/env python

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
                   , 'P': 'uri-path'
                   , 'I': 'uri-file'
                   , 'O': 'output'
                   }
    #try getting arguments
    try:
        opts, args = getopt.getopt( argv
                                  , "D:P:I:O: h"
                                  , [ "domain="
                                    , "uri-path="
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
        
        #check to see if the user passed both a sigular uri and uri file
        if options.get( 'uri-file', False ) and options.get( 'uri-path', False ):
            usage( "cannot specify a uri and a uri file" )
        
        #ensure we atleast have a domain
	if not options.get('domain',False):
            usage( "please set a domain")
                
        #see if we need to do anything extra
        if 'uri-file' in options:
            #get the uris from the file
            urls = urls_from_file( options.get( 'uri-file' ) )
        
        #make a single array of uris
        if 'uri-path' in options:
            urls = [ options.get( 'uri-path' ) ]
        
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

    usage += "\n====================================================================\n"
    usage += "\nPrintPal is a website to pdf application which utilizes wkhtmltopdf binary\n <http://code.google.com/p/wkhtmltopdf/>:\n"
    usage += "\nAvailable Commands:\n"
    usage += "\t-D <--domain>: Domain of website to print.\n"
    usage += "\t-P <--uri-path>: uri segment to use with domain\n"
    usage += "\t-I <--uri-file>: file of uri segments to use with domain ( ne wline delimited ).\n"
    usage += "\t-O <--output>: Path where the file should be saved to.\n"
    usage += "\n====================================================================\n"
    print usage
    sys.exit(0)   
    

#call our main app
main(sys.argv[1:])