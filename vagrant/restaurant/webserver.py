from BaseHTTPServer import BaseHTTPRequestHandler, HTTPServer

def main():
    try:
        port = 8080
        server = HTTPServer(('',port), webserverHandler)
        print "Web server running on port %s" % port
        server.serve_forver()


    except KeyboardInterrupt:

if __name__ == '__main__':
    main()
