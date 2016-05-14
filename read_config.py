#!/usr/bin/python

import csv,sys
import urllib2
import re
import datetime
import logging

def do_the_trick():

  with open(sys.argv[1]) as f:
    d = dict(filter(None, csv.reader(f)))
    urls = d.keys()
    search = d.values()
    for key in d:
      try:
        (TheUrl,String) = key,d[key]
        start = datetime.datetime.now()
        page = urllib2.urlopen(TheUrl).read()
        end = datetime.datetime.now()
        diff = end - start
        diff_in_second = int(round(diff.microseconds / 1000))
      except IOError, e:
        logging.warning('Cant read %s', TheUrl)
      else:
        matches = re.findall(String, page);
        if len(matches) == 0: 
          logging.info('I did not find anything')
        else:
          logging.info('Content Found: %s is in the %s, it took %s seconds to fetch.', String, TheUrl, diff_in_second)
  
