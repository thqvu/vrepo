import socket

devices = ['172.16.26.230', '172.16.26.231', '172.16.26.232',
           '172.16.26.233', '172.16.26.234', '172.16.26.235', '172.16.26.236']
port = 22

for device in devices:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        s.connect((device, port))
        s.shutdown(2)
        print("Port " + str(port) + " is open at " + device)
    except socket.error as e:
        print("Port " + str(port) + " is not open at " + device)
