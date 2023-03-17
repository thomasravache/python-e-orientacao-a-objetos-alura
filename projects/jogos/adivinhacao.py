print('******************')
print('Bem vindo no jogo de adivinhação!')
print('******************')

numero_secreto = 42

# tipo string
chute_tipo_string = input('Digite o seu número: ')
chute = int(chute_tipo_string)

print('Você digitou ', chute)

acertou = chute == numero_secreto
menor = chute < numero_secreto
maior = chute > numero_secreto

# Necessária a identação de 4 espaços, senão o python não entende. Ele se baseia na identação do código

if (acertou):
    print('Você acertou!')
else:
    if (maior):
        print('Seu chute foi maior que o número secreto')
    elif (menor):
        print('Seu chute foi menor que o número secreto')

print('Fim do jogo')
