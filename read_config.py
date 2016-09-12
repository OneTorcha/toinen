#!/usr/bin/python

import csv,sys
import urllib2,re
import datetime
import logging
import htmlGen

def do_the_trick(csv_file):
        
    with open(csv_file) as f:
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
                state = 0
                htmlGen.html_fill(state,String,TheUrl,diff_in_ms,sys.argv[2])
            else:
                matches = re.findall(String, page);
                if len(matches) == 0: 
                    logging.warning('Can\'t find %s from %s', String, TheUrl)
                    state = 1
                    htmlGen.html_fill(state,String,TheUrl,diff_in_ms,sys.argv[2])
                else:
                    logging.info('Content Found: %s is in the %s, it took %s ms to fetch.', String, TheUrl, diff_in_ms)
                    state = 2 
                    htmlGen.html_fill(state,String,TheUrl,diff_in_ms,sys.argv[2])
            # Lets make the index.html and change        
            htmlGen.index_fill(index,String) 
               
