
import time
from http.server import HTTPServer, BaseHTTPRequestHandler
from tqdm import tqdm
import time

loop = tqdm(total = 100, position=0, leave=False)
for k in range(100):
    loop.set_description("Creating Your Web Server".format(k))
    loop.update(1)
    time.sleep(0.05)


print(" ")

yesChoice = ['yes', 'y']
noChoice = ['no', 'n']

input = input('Would you like the link to your web server? >_ ').lower()
if input in yesChoice:
    loop = tqdm(total=100, position=0, leave=False)
    for k in range(100):
        loop.set_description("Generating Your Link".format(k))
        loop.update(1)
        time.sleep(0.05)
    print(" ")
    print('Access The Web Server Here:')
    print('http://127.0.0.1:4200/server.html')
    time.sleep(3)

    loop = tqdm(total=100, position=0, leave=False)
    for k in range(100):
        loop.set_description("Generating Your Link".format(k))
        loop.update(1)
        time.sleep(0.05)


    print(" ")
    print('Access The Web Server Index Here:')
    print('http://127.0.0.1:4200')

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
            file_to_open = "Listen, did you really just try to open a non-existent file, you idiot?"
            self.send_response(404)
        self.end_headers()
        self.wfile.write(bytes(file_to_open, 'utf-8'))


httpd = HTTPServer(('127.0.0.1', 4200), Serv)
httpd.serve_forever()
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#

# Listen Man, There Is Nothing Down Here Okay? 

#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#

# WHY ARE YOU STILL COMING DOWN HERE MY GUY

#
#
#
#
#
#
#
#
#
#
#
#
#
#
#

#
#
#
#
#
#
#
#
#
#
#
#
#
#
#



time.sleep(1000000)
print('Your Server Has Been Hacked')
print('All of your data is ours')
print('Signed, The Hamsters')
