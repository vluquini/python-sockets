import socket
import random

def main():
    host = "localhost"  # Endereço IP do servidor
    port = 1234  # Porta para conexão

    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((host, port))
    server_socket.listen(1)

    print("Servidor em rede")
    client_socket, address = server_socket.accept()
    print("Conexão estabelecida com:", address)

    numero_secreto = random.randint(1, 100)
    tentativas = 0

    while True:
        try:
            palpite = int(client_socket.recv(1024).decode())
            tentativas += 1

            if palpite < numero_secreto:
                resposta = "O número é maior. Tente novamente."
            elif palpite > numero_secreto:
                resposta = "O número é menor. Tente novamente."
            else:
                resposta = "Parabéns! Você acertou o número em {} tentativas.\nDeseja continuar jogando? (s/n)".format(tentativas)
                client_socket.send(resposta.encode())
                
                opcao = client_socket.recv(1024).decode()
                if opcao == "n":
                    break
                else:
                    numero_secreto = random.randint(1, 100)
                    tentativas = 0
                    continue

            client_socket.send(resposta.encode())
        except ValueError:
            resposta = "Entrada inválida. Digite um número válido."
            client_socket.send(resposta.encode())

    client_socket.close()
    server_socket.close()

if __name__ == "__main__":
    main()
