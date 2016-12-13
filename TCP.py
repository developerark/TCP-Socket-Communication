# Author Aswin Raj Kharel
# Copyright

import socket

class TCP:

	def __init__(self, host="127.0.0.1", port="8080"):
		self.__socketConnection = socket.socket()
		self.__socketConnection.bind((host, port))
		self.__socketConnection.listen(1)
		self.__connection, self.__address = socketConnection.accept()
		print "[+] Connection Made with " + str(address)
		self.startReceiving()

	def startReceiving(self):
		while True: 
			dataReceived = self.__connection.recv(1024)
			if not data:
				break
			


