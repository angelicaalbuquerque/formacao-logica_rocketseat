#  Aprendemos a aplicar variáveis, listas e estruturas condicionais 

perguntas = [ 
  ['Seu animal gosta de bananas?', 'macaco'], 
  ['Seu animal gosta de cenoura?', 'coelho'],
  ['Seu animal gosta de queijo?', 'rato'], 
  ['Seu animal gosta de bambu?', 'panda'], 
]

print('Pense em um animal...')

#para cada elemento da lista de perguntas, associo à variável pergunta
for pergunta in perguntas:
  resposta = input(f'{pergunta[0]} (s/n): ')
  if resposta.lower() == 's':
    print(f'Você pensou em {pergunta[1]}!')
    break
else:
  print('Poxa... não consegui adivinhar!')