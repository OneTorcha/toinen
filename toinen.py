#!/usr/bin/python

import logging,sys,os
import read_config,http_servu,htmlGen
import datetime, threading
from optparse import OptionParser
import time, subprocess
import argparse

def main():
    parser = argparse.ArgumentParser(description='toinen - simple http monitoring tool.')
    parser.add_argument('-i','--input', help='Input CSV file name',required=True)
    parser.add_argument('-p','--polltime',help='Polling time', required=True)
    args = parser.parse_args()    
    
    logging.basicConfig(level=logging.DEBUG,
                      format='%(asctime)s %(levelname)s %(message)s',
                      filename='toinen.log',
                      filemode='w')
      
    logging.info('Starting the monitoring rounds.')  
     
    subprocess.Popen("./http_servu.py", shell=True)
           
    while True:
        read_config.do_the_trick(sys.argv[2])
        time.sleep(int(sys.argv[4]))

if __name__ == '__main__':
    main()
# commit test
