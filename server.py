# Author Aswin Raj Kharel
# Copyright

# Server Code

import socket
import sys

arguments = sys.argv

# This function can be used to process the data received from the client the way you like to. Pseudo Method
def processData(data):
	return str(data).upper()

if __name__ == '__main__':
	
	# Connection Informations
	host = arguments[1]
	port = int(arguments[2])

	# Creating the connection. 
	socketObject = socket.socket()
	socketObject.bind((host, port))

	# Make the server to listen on the port
	socketObject.listen(1)

	connection, address = socketObject.accept()
	print "[+] Connection Established with " + str(address)

	# Infinite Loop to receive the data from the client
	while True:
		data = connection.recv(1024)
		if not data:
			break

		# Print data from user
		print "From Client: " + str(data)
		print "To Client: " + processData(data)
		connection.send(processData(data))

	# Close the connection once the connection is lost
	connection.close()



