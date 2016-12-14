# Author Aswin Raj Kharel
# Copyright

# Client Code

import socket

if __name__ == "__main__":

	# Connection Information
	host = '127.0.0.1'
	port = 8080

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




