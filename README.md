PrintPal.py
==========

Automated Site PDF Creation 

PrintPal is an html to pdf CLI utility written in Python. Its purpose is to 
easily take a domain with one or more urls and bundle each html page into one
pdf document utilizing wkhtmltopdf <http://code.google.com/p/wkhtmltopdf/>. 
    
Usage
---------

```
//create a simple page pdf of a site
$ python printpal.py -D example.com/index.html

//create a multi-page pdf of a site
$ python printpal.py -D example.com -I urls.txt

//create a pdf with a specified output
$python printpal.py -D example.com -O ~/Desktop/Sample.pdf
```

Available Commands
--------------------
```
-D <--domain>: Domain of website to print.
-I <--uri-file>: file of uri segments to use with domain ( newline delimited ).
-O <--output>: Path where the file should be saved to.
```

Version
---------
Author:    Chris Morris http://github.com/morriswchris

Date:      July 24 2013

version:   1.0.0

License
-------

Released under the MIT license.

