#!/usr/bin/python

import sys
import BaseHTTPServer
from SimpleHTTPServer import SimpleHTTPRequestHandler

# Just basic SimpleHTTPServer.

def start_http_server():

  HandlerClass = SimpleHTTPRequestHandler
  ServerClass  = BaseHTTPServer.HTTPServer
  Protocol     = "HTTP/1.0"
  port = 8000
  server_address = ('127.0.0.1', port)

  HandlerClass.protocol_version = Protocol
  httpd = ServerClass(server_address, HandlerClass)

  sa = httpd.socket.getsockname()
  print "HTTP at your service on", sa[0], "port", sa[1], "..."
  httpd.serve_forever()

def main():
  start_http_server()

if __name__ == '__main__':
  main()
