#!/bin/python3

# Sockets

import socket

HOST = '127.0.0.1'
PORT = 7777

'''
With a netcat listener on port 7777, the following code will connect to the listener and close immediately
'''
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # af_inet is ipv4, sock_stream is a port
s.connect((HOST,PORT))

