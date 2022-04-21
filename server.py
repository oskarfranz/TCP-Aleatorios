import nacl.utils
import socket

numbers = str(nacl.utils.random(128))

random = ''

for number in numbers:
    random += number.encode("utf-8").hex()

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server.bind((socket.gethostname(), 80))
server.listen(10)
# print(random)

while 1:
    client, address = server.accept()
    if(client):
        print("Conectado al cliente.")
        client.send(random.encode())
    else:
        print("Intentando conectar con el cliente...")