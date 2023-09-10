import socket

# socket obyekti yaratamiz
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bog'lanishni amalga oshirish uchun server manzilini va portni aniqlab olish kerak
server_address = ('127.0.0.1', 8000) # 127.0.0.1 - localhost deb ham ataladi

# Serverga bog'lanishni amalga oshirish
client_socket.connect(server_address)

# Serverga "file" so'zini jo'natamiz
client_socket.sendall('file'.encode())

# Faylni qabul qilamiz
file_data = client_socket.recv(1024)

# Faylni diskga yozamiz
with open('example.txt', 'wb') as f:
    f.write(file_data)

# Bog'lanishni yopish
client_socket.close()