#!/usr/bin/env python

import socket
import ntpath
import Tkinter, tkFileDialog

#TCP_PORT = 5005
BUFFER_SIZE = 1024
print "  _________              __           __    ___________.__.__             _________               __                   _______________  _______  _______ ._."
print " /   _____/ ____   ____ |  | __ _____/  |_  \_   _____/|__|  |   ____    /   _____/__.__. _______/  |_  ____   _____   \_____  \   _  \ \   _  \ \   _  \| |"
print " \_____  \ /  _ \_/ ___\|  |/ // __ \   __\  |    __)  |  |  | _/ __ \   \_____  <   |  |/  ___/\   __\/ __ \ /     \   /  ____/  /_\  \/  /_\  \/  /_\  \ |"
print " /        (  <_> )  \___|    <\  ___/|  |    |     \   |  |  |_\  ___/   /        \___  |\___ \  |  | \  ___/|  Y Y  \ /       \  \_/   \  \_/   \  \_/   \|"
print "/_______  /\____/ \___  >__|_ \\\\___  >__|    \___  /   |__|____/\___  > /_______  / ____/____  > |__|  \___  >__|_|  / \_______ \_____  /\_____  /\_____  /_"
print "        \/            \/     \/    \/            \/                 \/          \/\/         \/            \/      \/          \/     \/       \/       \/\/\n\n"

print "  ______  __       __   _______ .__   __. .___________."
print " /      ||  |     |  | |   ____||  \ |  | |           |"
print "|  ,----'|  |     |  | |  |__   |   \|  | `---|  |----`"
print "|  |     |  |     |  | |   __|  |  . `  |     |  | "
print "|  `----.|  `----.|  | |  |____ |  |\   |     |  |"
print " \______||_______||__| |_______||__| \__|     |__|"

#Ask for Connection Settings
TCP_IP = raw_input("Enter Server Address: ")
TCP_PORT = int(input("Enter Server Port: "))

print("\nPlease Select a file you'd like to upload.")

#Prompt User for file to upload
root = Tkinter.Tk()
root.withdraw()
file_path = tkFileDialog.askopenfilename()

#Open File in Binary format for stream
f = open(file_path,'rb')

#Check for successful file load
if f:
    print "File Loaded"
else:
    print "File Error"
filename = ntpath.basename(file_path)
#Look for connection at Socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((TCP_IP, TCP_PORT))

s.send(str(filename))
print "Sent: " + str(filename)

#Send read packet, and read in new packet. until file is done.
l = 1
while(l):
    l = f.read(BUFFER_SIZE)
    #print "Data Sent: " + str(l)
    s.send(l)

print "File upload complete!"
f.close()

#Close socket connection
s.close()

print "Thank you for your upload!"
