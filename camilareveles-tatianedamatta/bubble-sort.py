# Esse progama organiza as cartas em ordem numerica
cartas = [11, 18, 3, 1, 16, 12, 6, 19, 5, 0, 14, 4, 17, 9, 13, 7, 10, 15, 2, 8] # sao os termos 

N = 20 # numero de termos 

# i e j sao as posicoes dos elementos (termos), ou seja, as cartas em si. 
# iniciando em i, especificamos o range (intervalo), entre a primeira posicao (0), e a ultima (N-1), 
# em um intervalo de 1 em 1 (ou seja, para cada elemento).
# ja em j, iniciamos com i+1, pois o termo da primeira posicao ja foi indicado pelo primeiro "for i..."
# cada "for" serve para testar se "cartas[i] e maior que cartas[j]; em seguida, comecamos o teste:

for i in range(0, N - 1, 1): # encontrando a posicao dos termos na lista
    for j in range(i + 1, N, 1): # encontrando a posicao dos termos em j
        if cartas[i] > cartas[j]: # realizando o teste
            temp = cartas[i]
            cartas[i] = cartas[j]
            cartas[j] = temp

# se cartas[i] for maior que cartas[j], ou seja, se o primeiro termo for maior que o segundo, sera montada uma 
# nova variavel chamada temp para todo i maior que j.

print(cartas) # mostra as cartas organizadas em ordem numerica, depois do teste. 


print("Resultado do programa:", cartas) #mostra o resultado do programa, ou seja, organiza os numeros em ordem crescente

#agora, vamos selecionar os 5 maiores e os 5 menores valores:

#5 primeiros elementos:
primeiros_elementos=cartas[0:5:1]

#5 ultimos elementos:
#para selecionar os 5 ultimos: N e o numero de elementos; e 0 e o primeiro elemento. Entao, o ultimo sera N-1.
#portanto, o decimo quinto elemento sera N-6.

ultimos_elementos=cartas[N-6:N-1:1]

#para imprimir: 
print("5 primeiros elementos:", primeiros_elementos)
print("5 ultimos elementos", ultimos_elementos)
