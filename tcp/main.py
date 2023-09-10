import socket

# socket obyekti yaratamiz
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bog'lanish uchun port
server_address = ('127.0.0.1', 8000)

# server_socketni server_address ga bog'lash
server_socket.bind(server_address)

# Maxsus portda xizmat ko'rsatish uchun server_socketni eshitishni boshlaymiz
server_socket.listen(1)

while True:
    # Bog'lanish uchun kutish
    print('Waiting for a connection...')
    client_socket, client_address = server_socket.accept()

    # Klientdan kelgan ma'lumotlarni qabul qilamiz
    data = client_socket.recv(1024).decode().strip()

    if data == 'file':
        # Faylni ochish va o'qish uchun ochamiz
        with open('example.txt', 'rb') as f:
            file_data = f.read()

        # Faylni klientga yuboramiz
        client_socket.sendall(file_data)

    # Bog'lanishni yopamiz
    client_socket.close()
