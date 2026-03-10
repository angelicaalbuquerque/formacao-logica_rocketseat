# estruturas-repeticao

soma = 0
n = 1

print('Vamos somar de 1 a 10')

# while n <= 10:
#    soma = soma + n
#    n = n + 1
#    print(f'Soma: {soma}')
#    print(f'n: {n}')

for index in range(1,11):
    soma += index

print(f'A soma de 1 a 10 é: {soma}')