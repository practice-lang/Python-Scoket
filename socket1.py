import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server = "siru.zyx"


def pscan(port):
    try:
        s.connect((server, port))
        return True
    except:
        return False


for x in range(1, 9999):
    if pscan(x):
        print("Port", x, ' Open!')
    else:
        print("Port" + x+"is closed")
