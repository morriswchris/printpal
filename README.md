PrintPal.py
==========

Automated Site PDF Creation 

Commands
---------

```
//create a simple page pdf of a site
$ python printpal.py -D example.com/index.html

//create a multi-page pdf of a site
$ python printpal.py -D example.com -I csv_urls

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

License
-------

Released under the MIT license.

