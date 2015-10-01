# importar a biblioteca do python chamada matplotlib.pyplot com o apelido de plt
import matplotlib.pyplot as plt

# criar um programa para ordenar uma lista de numeros em ordem crescente
# numero de elementos da lista
n = 20
# elementos da lista
lista = [11, 18, 3, 1, 16, 12, 6, 19, 5, 0, 14, 4, 17, 9, 13, 7, 10, 15, 2, 8]
# plotar os graficos
plt.figure()
# plotar o grafico da lista de bolas pretas
plt.plot(range(0, n), lista, 'ok')
# nomear o grafico como 'principio'
plt.title("principio")
# nomear o eixo x como 'indice'
plt.xlabel("indice")
# nomear o eixo y como 'valor'
plt.ylabel ("valor")
# salvar o grafico na pasta fig como: 'grafico-inicial'
plt.savefig("fig/grafico-inicial.png")
plt.close()
# nova tarefa gerar graficos com o nome bubble-troca.png iniciando em troca
troca = 0 
      
# imprimir a lista em ordem original, denominada "Lista original"
print ("Lista original:", lista)
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
            # definir os graficos iniciando em bubble-troca-01
            troca = troca + 1             
            
            # plotar os graficos            
            plt.figure()
            # plotar os graficos de 0 a n relativos a lista com bolas pretas            
            plt.plot(range(0, n), lista, 'ok')
            plt.plot(i, lista [i], 'or')
            plt.plot(j, lista [j], 'ob')        
            # nomear o grafico com o titulo de 'principio'            
            plt.title("principio")
            # nomear o eixo x como 'indice'            
            plt.xlabel("indice")
            # nomear o eixo y como 'indice'            
            plt.ylabel ("valor")
            # salvar toda as figuras gerados como bubble-troca-n com n variando de 1 ate 99            
            plt.savefig("fig/bubble-troca-{}.png".format(troca))            
            plt.close()
# imprimir a lista em ordem crescente, denominada "Lista em ordem crescente"
print ("Lista em ordem crescente:", lista)

plt.figure()
plt.plot(range(0, n), lista, 'ok')
plt.title("principio")
plt.xlabel("indice")
plt.ylabel ("valor")
plt.savefig("fig/grafico-final.png")
plt.close()

# conjunto de 5 numeros da lista
lista [0 : 5] == [0, 1, 2, 3, 4]
# imprimir lista dos cinco maiores valores em ordem decrescente
print ("Cinco maiores valores:", lista [n : n - 5 : -1])
# imprimir lista dos cinco menores valores em ordem crescente
print ("Cinco menores valores:", lista [0 : n - 15])

# tarefa fazer o restante das iteraçoes agora com o bubble-sort-it-n.py com n variando de 1 a 190
it = 0 
for i in range(0, n-1, 1):
    # intervalos dos valores para j
    for j in range(i+1, n, 1):
        if lista [i] < lista [j]:
            temp = lista [i]
            lista [i] = lista [j]
            lista [j] = temp
            it = it + 1            
            plt.figure()
            # plotar os graficos de 0 a n relativos a lista com bolas pretas            
            plt.plot(range(0, n), lista, 'ok')
            plt.plot(i, lista [i], 'or')
            plt.plot(j, lista [j], 'ob')        
            # nomear o grafico com o titulo de 'principio'            
            plt.title("principio")
            # nomear o eixo x como 'indice'            
            plt.xlabel("indice")
            # nomear o eixo y como 'indice'            
            plt.ylabel ("valor")            
            plt.savefig("fig/bubble-it-{}.png".format(it))
            plt.close()