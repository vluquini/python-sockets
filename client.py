import socket

def main():
    host = "localhost"  # Endereço IP do servidor
    port = 1234  # Porta para conexão

    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((host, port))

    while True:
        try:
            palpite = input("Digite um número entre 1 e 100: ")
            client_socket.send(palpite.encode())

            resposta = client_socket.recv(1024).decode()
            print(resposta)

            if "Parabéns" in resposta:
                opcao = input().lower()
                client_socket.send(opcao.encode())
                if opcao == "n":
                    break
        except ValueError:
            print("Entrada inválida. Digite um número válido.")

    client_socket.close()

if __name__ == "__main__":
    main()
