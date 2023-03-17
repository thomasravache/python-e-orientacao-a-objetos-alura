print('******************')
print('Bem vindo no jogo de adivinhação!')
print('******************')

numero_secreto = 42

# tipo string
chute_tipo_string = input('Digite o seu número: ')
chute = int(chute_tipo_string)

print('Você digitou ', chute)

# Necessária a identação de 4 espaços, senão o python não entende. Ele se baseia na identação do código

if (chute == numero_secreto):
    print('Você acertou!')
else:
    print('Você errou!')
