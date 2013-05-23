#!/usr/bin/env python

#imports
import os
import sys
import getopt

def main(argv):
    #maping table
    map_commands = { 'D': 'domain'
                   , 'P': 'uri-path'
                   , 'I': 'uri-file'
                   }
    #try getting arguments
    try:
        opts, args = getopt.getopt( argv
                                  , "D:P:I:h"
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
    pdf(options)

def pdf(options):
	print options
	if not options.get('domain',False):
            usage( "please set a domain")
	#get uri from file if exists

	#setup command
	cmd = "wkhtmltopdf "+options.get('domain','')+"/"+options.get('uri-path',"")+" "+options.get('output',options.get('domain','')+'.pdf')
	os.system(cmd)
	sys.exit(0)

def usage( error_str ):
    usage = ""
    if error_str != "":
        usage += "\nThere was an issue with your command. Please review you statment against our list on commands!:\n"
        usage += "\t*"+error_str

    usage += "\n====================================================================\n"
    usage += "\nPrintPal is a website to pdf application which utilizes wkhtmltopdf:\n"
    usage += "\nAvailable Commands:\n"
    usage += "\t-D <--domain>: Domain of website to print.\n"
    usage += "\t-P <--uri-path>: uri segment to use with domain\n"
    usage += "\t-I <--uri-file>: file of uri segments to use with domain.\n"
    usage += "\n====================================================================\n"
    print usage
    sys.exit(0)
    
    

#call our main app
main(sys.argv[1:])