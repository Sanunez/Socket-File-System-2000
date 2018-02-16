#!/usr/bin/env python
import socket
import sys

TCP_IP = 'localhost'
TCP_PORT = 5005
BUFFER_SIZE = 1024

print "  _________              __           __    ___________.__.__             _________               __                   _______________  _______  _______ ._."
print " /   _____/ ____   ____ |  | __ _____/  |_  \_   _____/|__|  |   ____    /   _____/__.__. _______/  |_  ____   _____   \_____  \   _  \ \   _  \ \   _  \| |"
print " \_____  \ /  _ \_/ ___\|  |/ // __ \   __\  |    __)  |  |  | _/ __ \   \_____  <   |  |/  ___/\   __\/ __ \ /     \   /  ____/  /_\  \/  /_\  \/  /_\  \ |"
print " /        (  <_> )  \___|    <\  ___/|  |    |     \   |  |  |_\  ___/   /        \___  |\___ \  |  | \  ___/|  Y Y  \ /       \  \_/   \  \_/   \  \_/   \|"
print "/_______  /\____/ \___  >__|_ \\\\___  >__|    \___  /   |__|____/\___  > /_______  / ____/____  > |__|  \___  >__|_|  / \_______ \_____  /\_____  /\_____  /_"
print "        \/            \/     \/    \/            \/                 \/          \/\/         \/            \/      \/          \/     \/       \/       \/\/\n\n"
print "     _______. _______ .______     ____    ____  _______ .______  "
print "    /       ||   ____||   _  \    \   \  /   / |   ____||   _  \ "
print "   |   (----`|  |__   |  |_)  |    \   \/   /  |  |__   |  |_)  |"
print "    \   \    |   __|  |      /      \      /   |   __|  |      /     "
print ".----)   |   |  |____ |  |\  \----.  \    /    |  |____ |  |\  \----."
print "|_______/    |_______|| _| `._____|   \__/     |_______|| _| `._____|"
print "------------------------------------------"
print "Current Settings:"
print "Host IP: " + TCP_IP
print "Port: " + str(TCP_PORT)
print "------------------------------------------"

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((TCP_IP, TCP_PORT))
s.listen(1)
print "Server Listening for Clients....\n"
i = 1
while True:
    conn, address = s.accept()
    print "Connection established with: " + str(address) + "\n"

    filename = conn.recv(BUFFER_SIZE)
    print filename
    f = open(str(filename), "wb")
    i = i+1

    l=1
    while(l):
        l= conn.recv(BUFFER_SIZE)
        while(l):
            f.write(l)
            l= conn.recv(BUFFER_SIZE)
        f.close()
    conn.close()
s.close()

