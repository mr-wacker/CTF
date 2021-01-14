import socket

def getMessage(): 

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect(("docker.hackthebox.eu",31956))
    banner = s.recv(1024)
    #print(banner)
    s.send(b"1")
    message = s.recv(1024)
    return (message.decode("utf-8") )

#test = getMessage()

for i in range(15):
    print("cout:%d" % i)
    print(getMessage())