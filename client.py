import socket

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((socket.gethostname(), 80))
random = client.recv(128)
print("Elemento recibido: \n\n" + random.decode("utf-8"))