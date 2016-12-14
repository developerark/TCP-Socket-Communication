# Author Aswin Raj Kharel
# Copyright

# Client Code

import socket
import sys

arguments = sys.argv

if __name__ == "__main__":

	# Connection Information
	host = arguments[1]
	port = int(arguments[2])

	# Creating the connection
	socketObject = socket.socket()
	socketObject.connect((host, port))

	# Get the input from the user to send to the server
	input = raw_input("Input> ")

	# quit when q pressed
	while input != 'q':
		socketObject.send(input)
		data = socketObject.recv(1024)
		print 'From Server: ' + str(data)
		input = raw_input("Input> ")

	# Close the socket once done
	socketObject.close()




