# Tipos de dados

# Numéricos, texto, booleano
# estaticamente tipadas:
  #precisa declarar os tipos antes de usar
#Python é dinamicamente tipada:
  #não precisa declarar

#linguagens podem ser fracamente tipadas, como JS, onde voce combina tipos diferentes em operação e não dá problema. 

#Já o Python é fortemente tipado: apesar de declrar os tipos, não deixa eu trabalhar com eles juntos. Exemplo:
print(15 + "água") 
#TypeError: unsupported operand type(s) for +: 'int' and 'str'

x = 15
print(type(x))
#<class 'int'>
#Pyton enxerga tudo como classes e objetos. 

print(dir(x))
#O int traz junto metodos que consigo utilizar relacinados à variavel x.


