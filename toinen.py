#!/usr/bin/python

import logging,sys
import read_config,http_servu
import datetime, threading
from optparse import OptionParser
import time, subprocess



def main():

  logging.basicConfig(level=logging.DEBUG,
                      format='%(asctime)s %(levelname)s %(message)s',
                      filename='toinen.log',
                      filemode='w')
  logging.basicConfig(format='%(asctime)s %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p')
  logging.info('Starting the monitoring rounds.')  

     
  #subprocess.call("./http_servu.py")

  while True:
    read_config.do_the_trick() 
    time.sleep(int(sys.argv[2]))



if __name__ == '__main__':
    main()




