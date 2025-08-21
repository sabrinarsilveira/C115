import socket

HOST = '127.0.0.1'
PORT = 5000

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as cliente:
    cliente.connect((HOST, PORT))

    for _ in range(2):  # duas questões
        # Recebe a questão
        dados = cliente.recv(1024).decode()
        print(dados)

        # Digita resposta
        resposta = input("Digite o número da alternativa: ")
        cliente.sendall(resposta.encode())

    # Recebe resumo final
    resumo = cliente.recv(1024).decode()
    print(resumo)
