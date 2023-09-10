import socket

# Yangi socket obyekti yaratamiz
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bog'lanish uchun serverimizning manzilini va portni aniqlab olish kerak
server_address = ('127.0.0.1', 8000) # 127.0.0.1 - localhost deb ham ataladi

# Serverimizni portiga bog'lash
server_socket.bind(server_address)

# Serverimizni tinglash
server_socket.listen()

while True:
    print("Klientni kuting...")
    # Klientning bog'lanish so'rovini qabul qilish
    client_socket, client_address = server_socket.accept()

    # Klientning manzilini konsolga chiqaramiz
    print(f"{client_address[0]}:{client_address[1]} dan so'rov qilindi!")

    # Klientdan fayl nomini olish
    filename = client_socket.recv(1024).decode()

    # Faylni o'qish rejimida ochish
    with open(filename, 'rb') as f:
        # Faylni bajarish va klientga yuborish
        data = f.read(1024)
        while data:
            client_socket.send(data)
            data = f.read(1024)

    # Bog'lanishni yopish
    client_socket.close()

