#!/usr/bin/python

import csv,sys
import urllib2,re
import datetime
import logging
import htmlGen

def do_the_trick():
        
    with open(sys.argv[1]) as f:
        d = dict(filter(None, csv.reader(f)))
        for key in d:
            try:
                (TheUrl,String) = key,d[key]
                index = d.keys().index(key) # get dict index for html regex 
                start = datetime.datetime.now()
                page = urllib2.urlopen(TheUrl).read()
                end = datetime.datetime.now()
                diff = end - start
                diff_in_ms = int(round(diff.microseconds / 1000))
                matches = re.findall(String, page);
                
            except IOError, e:
                logging.warning('Can\'t read %s', TheUrl)
                htmlGen.html_fill("No Conn")
            else:
                matches = re.findall(String, page);
                if len(matches) == 0: 
                    logging.info('Can\'t find %s from %s', String, TheUrl)
                    htmlGen.html_fill("No KeyWord")
                else:
                    logging.info('Content Found: %s is in the %s, it took %s ms to fetch.', String, TheUrl, diff_in_ms)
                    #print(index,TheUrl)
                    htmlGen.html_fill(diff_in_ms)
                    
