#!/usr/bin/env python

import socket
import re
import time

# Standard socket stuff:
host = ''  # do we need socket.gethostname() ?
port = 1234
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind((host, port))
sock.listen(1)  # don't queue up any requests

# Loop forever, listening for requests:
while True:
    csock, caddr = sock.accept()
    print "Connection from: " + `caddr`
    req = csock.recv(1024)  # get the request, 1kB max
    # Look in the first line of the request for a move command
    # A move command should be e.g. 'http://server/move?a=90'
    match = re.match('GET /avatoken=(\d+)\sHTTP/1', req)
    if match:
        angle = match.group(1)
        output = str(req.replace("\n","").replace("\r","\t"))
        with open("ava_log_file.txt", "a") as logfile:
            logfile.write(str(time.time()) + ","+angle+","+output+"\n")
            logfile.close()
        print "Token received: " + angle + "\n"
        csock.sendall("""HTTP/1.0 200 OK
Content-Type: text/html

<html>
<head>
<title>Success</title>
</head>
<body>
Golly darn and dang dabbit
</body>
</html>
""")
    else:
        # If there was no recognised command then return a 404 (page not found)
        print "Returning 404"
        csock.sendall("HTTP/1.0 404 Not Found\r\n")
    csock.close()