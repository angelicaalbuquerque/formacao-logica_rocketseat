#  Aprendemos a aplicar variáveis, listas e estruturas condicionais 

perguntas = [ 
  ['Seu animal gosta de bananas?', 'macaco'], 
  ['Seu animal gosta de cenoura?', 'coelho'],
  ['Seu animal gosta de queijo?', 'rato'], 
  ['Seu animal gosta de bambu?', 'panda'], 
]


while True:
  print('Pense em um animal...')

  acertou = False

  for pergunta in perguntas:
    resposta = input(f'{pergunta[0]} (s/n): ')
    if resposta.lower() == 's':
      print(f'Você pensou em {pergunta[1]}!')
      acertou = True
      break

  if not acertou:
    animal = input('Desisto! Em qual animal você pensou? ')
    novaPergunta = input('Qual pergunta você faria para identificar esse animal? ')
    perguntas.append([novaPergunta, animal])

  resposta = input('Quer jogar de novo? [s/n]: ')
  if resposta.lower() != 's':
    print('Foi bom jogar com você!')
    break



