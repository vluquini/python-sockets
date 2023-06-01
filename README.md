# Jogo de avidinhação em Python via Sockets
Este jogo é um simples jogo de adivinhação em que o jogador tenta adivinhar um número entre 1 e 100 escolhido aleatoriamente pelo programa. O jogo consiste em dois programas, um servidor e um cliente, que se comunicam via rede.

## Requisitos
Para jogar o jogo, você precisa ter o Python instalado no seu computador.

## Como jogar
- Execute o programa servidor.py em um terminal.
- Execute o programa cliente.py em outro terminal ou em outra máquina na mesma rede.
- O programa cliente solicita um palpite ao usuário, que deve ser um número inteiro entre 1 e 100.
- O programa cliente envia o palpite para o servidor.
- O servidor responde com uma mensagem indicando se o palpite é maior ou menor do que o número secreto.
- Repita os passos 3 a 5 até acertar o número.
- Se o jogador acertar o número, o servidor pergunta se o jogador deseja continuar jogando. 
- Se o jogador digitar "s", o jogo recomeça com um novo número secreto. Se o jogador digitar "n", o jogo termina.