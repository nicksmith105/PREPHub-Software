import bluetooth
import critical

serverSocket = bluetooth.BluetoothSocket( bluetooth.RFCOMM )
port = 1
backlog = 1
serverSocket.bind(('b8:27:eb:3d:ee:57',port))
print(port)
serverSocket.listen(backlog)

clientSocket, address = serverSocket.accept()
print("Accepted BT Connection from", address)
while 1:
    data = clientSocket.recv(1024)
    print("***Connected***")
    if data:
        print("Recieved: ", data)
        if data == b'0':
            print("Emergency Off: ", data)
            critical.off()
        elif data == b'q':
            break
        else:
            print("Run for the hills!")
            critical.warning()
            time.wait(1)

clientSocket.close()
serverSocket.close()
