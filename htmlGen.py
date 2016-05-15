
import sys,os
import csv,re 
import fileinput,string
import datetime
from webbrowser import open_new_tab


# for future use
def html_skel(): 
     
    h_reader = csv.reader(open(sys.argv[1]))
    html_file = open("index.html","w")
    rownum = 0
    html_file.write('<table>' + '\n')
    # Read a single row from the CSV file
    for row in h_reader: 
        html_file.write('<tr>' + '\n')	
        for column in row:
            html_file.write('<td>' + column + '</td>' )
        html_file.write('<td>' + str(rownum) + '</td>' + '\n')    
        html_file.write('</tr>' + '\n')
        rownum += 1
    html_file.write('</table>' + '\n')
    html_file.close

# To Creata separate monitoing window fro each site.
def html_fill(state,string,url,msec,refresh_time): 
      
    now = datetime.datetime.today().strftime("%Y%m%d-%H%M%S")

    filename = string + '.html'
    f = open(filename,'w')
    if state == 0 :
        wrapper = """<html>
              <head>
                <title>Monitoring page for %s</title>
                <meta http-equiv="refresh" content="%s">
              </head>
              <body>
                <p>Monitored HTML page: %s is Down!</p>
                <p>It took %s ms to check.</p>
                <p>The keyword %s was not there.</p>
                <p><font size="2">The page refeshes automatically.</font></p>
              </body>
              </html>"""
        whole = wrapper % (url, refresh_time, url, msec, string)
        f.write(whole)
        f.close()
    elif state == 1 :
        wrapper = """<html>
              <head>
                <title>Monitoring page for %s</title>
                <meta http-equiv="refresh" content="%s">
              </head>
              <body>
                <p>Monitored HTML page: %s is UP!</p>
                <p>It took %s ms to check.</p>
                <p>The keyword %s was not there.</p>
                <p><font size="2">The page refeshes automatically.</font></p>
              </body>
              </html>"""
        whole = wrapper % (url, refresh_time, url, msec, string)
        f.write(whole)
        f.close()
    elif state == 2 :
        wrapper = """<html>
              <head>
                <title>Monitoring page for %s</title>
                <meta http-equiv="refresh" content="%s">
              </head>
              <body>
                <p>Monitored HTML page: %s is UP!</p>
                <p>It took %s ms to check.</p>
                <p>The keyword %s was there.</p>
                <p><font size="2">The page refeshes automatically.</font></p>
              </body>
              </html>"""
        whole = wrapper % (url, refresh_time, url, msec, string)
        f.write(whole)
        f.close()
    
# hack to make index.html work at least some way.
def index_fill(ind,string):
        
    target_file = 'index.html'
    
    if os.path.isfile(target_file) :
        template_file = 'index.html'
    else:
        template_file = 'findex.html'
    
    indeksi = str(ind)
    filedata = None
    with open(template_file, 'r') as tfile :
        filedata = tfile.read()
        found = False
        for line in tfile:
            if string in line: 
                found = True
        if not found:
            filedata = filedata.replace(indeksi, string+'.html')
            with open(target_file, 'w') as file:
                file.write(filedata)