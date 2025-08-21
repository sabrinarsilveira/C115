import socket

# Questões e gabarito
questoes = [
    {
        "pergunta": "Qual é a capital da Itália?",
        "opcoes": ["Roma", "Paris", "Lisboa", "Londres"],
        "resposta": "Roma"
    },
    {
        "pergunta": "Qual é a capital do Japão?",
        "opcoes": ["Tóquio", "Pequim", "Seul", "Bangkok"],
        "resposta": "Tóquio"
    }
]

HOST = '127.0.0.1'
PORT = 5000

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as servidor:
    servidor.bind((HOST, PORT))
    servidor.listen()
    print("Servidor aguardando conexão...")

    conn, addr = servidor.accept()
    with conn:
        print(f"Conectado por {addr}")
        respostas_cliente = []
        resultados = []

        for q in questoes:
            # Monta a questão em formato de texto
            mensagem = f"{q['pergunta']}\n"
            for i, opcao in enumerate(q["opcoes"], start=1):
                mensagem += f"{i}) {opcao}\n"

            # Envia questão
            conn.sendall(mensagem.encode())

            # Recebe resposta do cliente
            resposta = conn.recv(1024).decode().strip()
            respostas_cliente.append(resposta)

            # Verifica acerto/erro
            try:
                resposta_index = int(resposta) - 1
                if q["opcoes"][resposta_index] == q["resposta"]:
                    resultados.append("Acertou")
                else:
                    resultados.append("Errou")
            except:
                resultados.append("Resposta inválida")

        # Calcula total de acertos
        acertos = resultados.count("Acertou")
        resumo = f"\nVocê acertou {acertos} de {len(questoes)} questões.\n"
        for i, r in enumerate(resultados, start=1):
            resumo += f"Questão {i}: {r}\n"

        conn.sendall(resumo.encode())
        print("Respostas enviadas ao cliente.")
