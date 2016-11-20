from django.shortcuts import render
from django.http import HttpResponse
import socket
import sys
from threading import *
import time


serversocket = socket.socket()
host = 'localhost'
port = 9000
serversocket.bind((host, port))


class client(Thread):
	global position
	def __init__(self, socket, address):
		Thread.__init__(self)
		self.sock = socket
		self.addr = address
		self.start()

	def run(self):
		while 1:
			mes = self.sock.recv(1024).decode()
			print(mes)
			
			if(mes[0] == 1):
				self.sock.send("Turn on")
			elif(mes[0] == 2):
				self.sock.send("Status is")
			else:
				print("Error")
			
			self.sock.send(b'Oi you sent something to me')




def index(request):
	serversocket.listen(5)
	print ('server started and listening')
	while 1:

		clientsocket, address = serversocket.accept()
		client(clientsocket, address)


	return HttpResponse(mes)
