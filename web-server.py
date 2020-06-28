
import time
from http.server import HTTPServer, BaseHTTPRequestHandler

print('Creating..........')
time.sleep(0.100)
print('Creating..........')
time.sleep(0.100)
print('Creating..........')
time.sleep(0.100)
print('Creating..........')
time.sleep(0.100)
print('Creating..........')
time.sleep(0.100)
print('Creating..........')
time.sleep(0.100)
print('Creating..........')
time.sleep(0.100)
print('Creating..........')
time.sleep(0.100)
print('Creating..........')
time.sleep(0.100)
print('Creating..........')
time.sleep(0.100)
print('Creating..........')
time.sleep(0.100)
print('Creating..........')
time.sleep(0.100)
print('Creating..........')
time.sleep(0.100)
print('Creating..........')
time.sleep(0.300)
print('Initializing...')
time.sleep(0.100)
print('Initializing...')
time.sleep(0.100)
print('Initializing...')
time.sleep(0.100)
print('Initializing...')
time.sleep(0.100)
print('Initializing...')
time.sleep(2)


yesChoice = ['yes', 'y']
noChoice = ['no', 'n']

input = input('Would you like the link to your web server? >_ ').lower()
if input in yesChoice:
    time.sleep(0.100)
    print("Generating...")
    time.sleep(0.100)
    time.sleep(0.100)
    print("Generating...")
    time.sleep(0.100)
    time.sleep(0.100)
    print("Generating...")
    time.sleep(0.100)
    time.sleep(0.100)
    print("Generating...")
    time.sleep(0.100)
    time.sleep(0.100)
    print("Generating...")
    time.sleep(0.100)
    print('Access The Web Server Here:')
    print('http://localhost:8080/server.html')

    time.sleep(0.100)
    print("Generating Index Link...")
    time.sleep(0.100)
    print("Generating Index Link...")
    time.sleep(0.100)
    print("Generating Index Link...")
    time.sleep(0.100)
    print('Access The Web Server Index Here:')
    print('http://localhost:8080/index.html')

elif input in noChoice:
    print('Okay, Thanks For Using Web Server Creator!_')

else:
    exit('I\'m sorry, You entered the wrong choice(s). The choices were: "yes" , "y" , "no" and "n". Please re-run Web Server Creator')

class Serv(BaseHTTPRequestHandler):

    def do_GET(self):
        if self.path == '/':
            self.path = '/index.html'
        try:
            file_to_open = open(self.path[1:]).read()
            self.send_response(200)
        except:
            file_to_open = "File not found"
            self.send_response(404)
        self.end_headers()
        self.wfile.write(bytes(file_to_open, 'utf-8'))


httpd = HTTPServer(('localhost', 8080), Serv)
httpd.serve_forever()

