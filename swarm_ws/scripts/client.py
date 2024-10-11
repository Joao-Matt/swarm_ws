# Client sends info to server
import bluetooth

bd_addr = "E4:5F:01:FC:47:8E" # The address from the server Raspberry Pi
port = 1

sock = bluetooth.BluetoothSocket(bluetooth.RFCOMM)
sock.connect((bd_addr, port))
print()

while True:
    data = input("Send: ")
    if not data:
        break
    sock.send(data)

sock.close()
