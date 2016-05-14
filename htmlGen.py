
import sys,os
import csv,re 
import fileinput,string
import datetime
from webbrowser import open_new_tab



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

def html_fill(state,string,url,msec):
      
    now = datetime.datetime.today().strftime("%Y%m%d-%H%M%S")

    filename = string + '.html'
    f = open(filename,'w')
    if state == 0 :
        wrapper = """<html>
              <head>
                <title>Monitoring page for %s</title>
                <meta http-equiv="refresh" content="5">
              </head>
              <body>
                <p>Monitored HTML page: %s is Down!</p>
                <p>It took %s ms to check.</p>
                <p>The keyword %s was not there.</p>
                <p><font size="2">The page refeshes automatically every 5 seconds.</font></p>
              </body>
              </html>"""
        whole = wrapper % (url, url, msec, string)
        f.write(whole)
        f.close()
    elif state == 1 :
        wrapper = """<html>
              <head>
                <title>Monitoring page for %s</title>
                <meta http-equiv="refresh" content="5">
              </head>
              <body>
                <p>Monitored HTML page: %s is UP!</p>
                <p>It took %s ms to check.</p>
                <p>The keyword %s was not there.</p>
                <p><font size="2">The page refeshes automatically every 5 seconds.</font></p>
              </body>
              </html>"""
        whole = wrapper % (url, url, msec, string)
        f.write(whole)
        f.close()
    elif state == 2 :
        wrapper = """<html>
              <head>
                <title>Monitoring page for %s</title>
                <meta http-equiv="refresh" content="5">
              </head>
              <body>
                <p>Monitored HTML page: %s is UP!</p>
                <p>It took %s ms to check.</p>
                <p>The keyword %s was there.</p>
                <p><font size="2">The page refeshes automatically every 5 seconds.</font></p>
              </body>
              </html>"""
        whole = wrapper % (url, url, msec, string)
        f.write(whole)
        f.close()
    
    
def index_fill(string):
    

    filename = 'index.html'    
    f1 = open(filename,'rw')
    for line in f1:
        print(line)
        print(string)
        
##        if line.contains(string):
##            print("on jo %s") %string
##        else:
##            f = open(filename,'a')
##            wrapper = """ <p><iframe src="%s.html" seamless></iframe></p>"""
##                    
##            whole = wrapper % (string)
##            f.write(whole+ '\n')
##            f.close()
##    