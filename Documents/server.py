import socket


ascii_art = '''\n███████╗ ██████╗  ██████╗██╗  ██╗███████╗████████╗     ██████╗ █████╗ ██╗      ██████╗██╗   ██╗██╗      █████╗ ████████╗ ██████╗ ██████╗ 
██╔════╝██╔═══██╗██╔════╝██║ ██╔╝██╔════╝╚══██╔══╝    ██╔════╝██╔══██╗██║     ██╔════╝██║   ██║██║     ██╔══██╗╚══██╔══╝██╔═══██╗██╔══██╗
███████╗██║   ██║██║     █████╔╝ █████╗     ██║       ██║     ███████║██║     ██║     ██║   ██║██║     ███████║   ██║   ██║   ██║██████╔╝
╚════██║██║   ██║██║     ██╔═██╗ ██╔══╝     ██║       ██║     ██╔══██║██║     ██║     ██║   ██║██║     ██╔══██║   ██║   ██║   ██║██╔══██╗
███████║╚██████╔╝╚██████╗██║  ██╗███████╗   ██║       ╚██████╗██║  ██║███████╗╚██████╗╚██████╔╝███████╗██║  ██║   ██║   ╚██████╔╝██║  ██║
╚══════╝ ╚═════╝  ╚═════╝╚═╝  ╚═╝╚══════╝   ╚═╝        ╚═════╝╚═╝  ╚═╝╚══════╝ ╚═════╝ ╚═════╝ ╚══════╝╚═╝  ╚═╝   ╚═╝    ╚═════╝ ╚═╝  ╚═╝'''
class SERVER:
    def __init__(self,host,port):
        self.host = host
        self.port = port

    def start(self):
        self.server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        self.server.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
        self.server.bind((self.host,self.port))
        self.server.listen(1)
        print("Server is Listening..")
        client,add = self.server.accept()
        print(f'[CONNECTION] from IP: {add[0]} PORT: {str(add[1])}')

        print('add ',add)
        print('socket ',socket)
        client.send(bytes(ascii_art,'utf-8'))
        while True:
            try:
                #First Value send to client
                first = 'Enter Your First Value (x): '
                encode1 = bytes(first,'utf-8')
                client.send(encode1)
                #Value recevied as bytes and encode string into utf-8 which converted in float
                first_value = float(client.recv(1024))
                #second value send to client
                second = 'Enter your second value (y): '
                client.send(bytes(second,'utf-8'))
                #second value received from client which is converted into string and encoded in utf-8 
                second_value = float(client.recv(2048).decode('utf-8')) #converting string to float
                #Operation send to clinet
                operator = 'Choose your Arthimetic operator:\n\t1. +\n\t2. -\n\t3. *\n\t4. /\n\t5. %'    
                mssg_encode = bytes(operator, 'utf-8')
                client.send(mssg_encode)
                operator2 = client.recv(1024).decode('utf-8')
                if operator2 == '+' or operator2=='1':
                    result = first_value +second_value
                    result1 = bytes(str(result),'utf-8')
                    client.send(result1)
                elif operator2 == '-' or operator2=='2' :
                    result = first_value - second_value
                    result1 = bytes(str(result),'utf-8')
                    client.send(result1)
                elif operator2 == '*' or operator2=='3':
                    result = first_value * second_value
                    result1 = bytes(str(result),'utf-8')
                    client.send(result1)
                elif operator2 == '/' or operator2=='4':
                    if second_value == 0:
                        client.send(bytes('Infinity','utf-8'))
                    else:
                        result = first_value / second_value
                        result1 = bytes(str(result),'utf-8')
                        client.send(result1)
                elif operator2 == '%' or operator2=='5':
                    result = first_value % second_value
                    result1 = bytes(str(result),'utf-8')
                    client.send(result1)
                else:
                    print('Further updates are coming ')
                    

            except ValueError:
                print('\n\t......................Terminating...........................')
                break
                
            except KeyboardInterrupt:
                break

        self.server.close()

s = SERVER('localhost',8888)
s.start()
