# criar um programa para ordenar uma lista de numeros em ordem crescente
# numero de elementos da lista

n = 20
# elementos da lista
lista = [11, 18, 3, 1, 16, 12, 6, 19, 5, 0, 14, 4, 17, 9, 13, 7, 10, 15, 2, 8]
# intervalos dos valores para i
for i in range(0, n-1, 1):
    # intervalos dos valores para j
    for j in range(i+1, n, 1):
        # comparacao do elemento i com o elemento j, se o elemento i for maior que o j fazer:
	if lista [i] > lista [j]:
            # mover o elemento i para o local temp
            temp = lista [i]
            # mover o elemento do local j para o local i
	    lista [i] = lista [j]
            # mover o elemento do local temp para o local j 
	    lista [j] = temp
# mostrar o resultado
print(lista)
