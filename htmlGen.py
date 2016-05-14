
import sys,os
import csv,re 
import fileinput,string


def html_skel():
     
    h_reader = csv.reader(open(sys.argv[1]))
    html_file = open("index.html","w")
    rownum = 0
    html_file.write('<table>' + '\n')
    for row in h_reader: # Read a single row from the CSV file
        html_file.write('<tr>' + '\n')	
        for column in row:
            html_file.write('<td>' + column + '</td>' )
        html_file.write('<td>' + str(rownum) + '</td>' + '\n')    
        html_file.write('</tr>' + '\n')
        rownum += 1
    html_file.write('</table>' + '\n')
    html_file.close

def html_fill(msec):
   
    return 