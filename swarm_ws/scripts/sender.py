# Bluetooth client (sender) on the other Raspberry Pi

import bluetooth

def get_rssi(remote_addr):
    # This function uses the hcitool command to get the RSSI of a remote device
    cmd = f"hcitool rssi {remote_addr}"
    result = subprocess.check_output(cmd, shell=True).decode("utf-8")
    rssi_value = result.split(":")[-1].strip()
    return rssi_value

server_address = "E4:5F:01:FC:47:8E"  # MAC address of the server (receiver) Raspberry Pi
port = 1  # Use the same port as defined in the server

client_sock = bluetooth.BluetoothSocket(bluetooth.RFCOMM)
client_sock.connect((server_address, port))

# Get the RSSI of the server (RPI A) and send it
rssi = get_rssi(server_address)
client_sock.send(rssi)

client_sock.close()
