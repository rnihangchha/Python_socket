import socket
import time
client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
client.connect(('localhost',8888))
ascii_art = client.recv(2048).decode('utf-8')
print(ascii_art)
time.sleep(3)

print('sucessfully connected')
while True:
    try:
        first = client.recv(1024).decode('utf-8')
        print(first)
        first_input = float(input(">> "))
        
        client.send(bytes(str(first_input),'utf-8'))

        second = client.recv(1024).decode('utf-8')
        print(second)
        second_input = float(input(">> "))
        
        client.send(bytes(str(second_input),'utf-8'))


        message = client.recv(2048).decode('utf-8')
        print(message)
        mssg = input('>> ')
        mssg_encoded = bytes(mssg,'utf-8')
        client.send(mssg_encoded)
        second_message = client.recv(2048).decode('utf-8')
        print(second_message)
    except KeyboardInterrupt:
        break