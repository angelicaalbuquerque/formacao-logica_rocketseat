# arrays

x = [40, 20, 50, 30]
print(x)
print(x[1]) #mostra qual numero está na posição desejada

x.append(10) #append: adiciona no final
print(x)

x.sort() #sort: ordena em ordem crescente
print(x)

x.reverse() #reverse: inverte a ordem da lista
print(x)

x.pop() #pop: retira o último item da lista
print(x)

x.insert(1,15) #insert: insere na posição 1 o numero 15, jogando pra frente o que antes era a posição do numero 40
print(x)

x.insert(1,6) #ele vai empurrando a lista pra frente
print(x)

x.sort()
print(x)

x.insert(3, [1,2,3]) #inseriu na posição 3 uma lista
print(x)
print(x[3]) #mostra x na posição 3, que é o array inserido
print(x[3][1]) #mostra x na posição 3, na posição 1 do array inserido