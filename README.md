# Prática de introdução ao Python

Parte do curso
[Matemática Especial I](http://www.leouieda.com/matematica-especial/)
da [UERJ](http://www.uerj.br/).

Ministrado por [Leonardo Uieda](http://www.leouieda.com/).

## Objetivos

* Aprender os conceitos básicos de programação: variáveis, loops e condicionais
* Usar esses conceitos aplicados a linguagem Python
* Exercitar o uso do `git` para controle de versão
* Expandir o conhecimento adquirido para conceitos mais avançados de Python:
  leitura de arquivos e gráficos simples

## Preparação

Faça um fork do repositório da prática para sua conta no Github.

![](https://raw.githubusercontent.com/leouieda/mat-esp-python-intro/master/images/fork-button.jpg)

O fork é uma cópia do repositório na sua conta, como um clone mas que ficou
online.  Vocês vão fazer mudanças e colocar a solução da prática em uma pasta
nesse seu fork.  Dessa vez, vocês vão submeter suas respostas para mim como um
[Pull Request](https://help.github.com/articles/using-pull-requests/) (mais
sobre isso no final da prática).

Por enquanto, vocês vão utilizar o seu fork como o remoto.  Adicione os outros
membros do grupo como colaboradores no projeto (Settings > Collaborators) para
que eles possam fazer `git push` para seu fork.  Depois, faça um clone do fork
para seu computador para cada membro.  Não esqueça de configurar o git para
cada clone.

Comandos importantes para lembrar:

* `git clone ORIGINAL DESTINO`
* `git config user.name "Meu Nome Completo"`
* `git config user.email meu@email.com`
* `git add nome_do_arquivo.meh`
* `git commit -m "Uma mensagem bem informativa sobre o que eu fiz"`
* `git push origin master`
* `git pull origin master`
* `git remote -v`
* Se esquecer o `-m` no `git commit` e entrar no editor de texto Vim: `Esc` e
  depois `:q!`.

## Tarefa 1

### Leitura recomendada

* http://software-carpentry.org/v4/python/basics.html
* http://software-carpentry.org/v4/python/flow.html

### Conceitos aplicados

* Variáveis: `a = 1`, `b = "bla bla bla"`
* Listas: `lista = [1, 2, 5, 21, 42]`
* Loops: `for i in range(0, N, 1):`
* Condicionais: `if a > b:`
* Imprimir para a tela: `print("Resultado do programa:", a)` (dica: `a` pode
  ser qualquer variável, inclusive uma lista)
* Comentários: `# Linhas começando com '#' são comentários`
* Executar comandos de um arquivo com `$ python arquivo.py`

### Instruções

Escolha um dos membros do grupo:

* Crie uma pasta com os primeiros nomes dos integrantes do grupo:
  `aluno1-aluno2-aluno3` dentro do repositório
* **Todos os arquivos que você fizer durante a prática devem ser colocados
  nessa pasta**
* Crie um arquivo chamado `bubble-sort.py`
* Coloque no arquivo o código Python para executar o bubble sort
* Seu programa deve organizar a seguinte lista:
  `[11, 18, 3, 1, 16, 12, 6, 19, 5, 0, 14, 4, 17, 9, 13, 7, 10, 15, 2, 8]`
* Coloque comentários que explicar cada linha do código. Lembre-se de explicar
  **"por que"** além de "o que"

Troque o membro do grupo:

* Modifique o programa para:
  * O programa deve imprimir **antes de começar o algoritmo**:
    `Lista original: [n1, n2, n3, ..., nN]` substituindo pelos valores da lista
    acima
  * Ao final, o programa deve imprimir a lista organizada em uma nova linha
    como: `Lista em ordem crescente: [n1, n2, ...]`
* Lembre-se de colocar comentários explicando suas linhas de código

Troque o membro do grupo:

* Modifique o programa para que imprima ao final os 5 maiores e os 5
  menores valores em linhas separadas:
  `Cinco maiores valores: [19, 18, 17, 16, 15]` e
  `Cinco menores valores: [0, 1, 2, 3, 4]`

Dicas:

* **Não esqueça de fazer as alterações em seu clone pessoal.**
* **Use `git commit` com frequência.**

### Resultado esperado

Você deve ter um arquivo `bubble-sort.py` com o código que desenvolvemos em
aula e seus comentários explicando cada linha de código.  Quando executado com
`$ python bubble-sort.py`, seu programa deverá imprimir na tela:

    Lista original: [11, 18, 3, 1, 16, 12, 6, 19, 5, 0, 14, 4, 17, 9, 13, 7, 10, 15, 2, 8]
    Lista em ordem crescente: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19]
    Cinco maiores valores: [19, 18, 17, 16, 15]
    Cinco menores valores: [0, 1, 2, 3, 4]


## Tarefa 2

### Leitura recomendada

* http://scipy-lectures.github.io/intro/matplotlib/matplotlib.html
* http://matplotlib.org/gallery.html

### Conceitos aplicados

* Criação de figuras com a biblioteca [matplotlib](http://matplotlib.org/)
* Carregar bibliotecas de funções: `import matplotlib.pyplot as plt`
* Criar uma figura vazia: `plt.figure()`
* Desenhar um gráfico de pontos ou linhas: `plt.plot(x, y, 'ok')` ou
  `plt.plot(x, y, '-k')`
* Colocar títulos no gráfico e eixos: `plt.title("Titulo")` e
  `plt.xlabel("x eh tal coisa")`
* Salvar a figura: `plt.savefig("nome-do-arquivo.png")`
* Inserir valores em *strings* (texto):
  `"Matematica {} - Turma {}".format("Especial", 1)` resulta em
  `"Matematica Especial - Turma 1"`

### Instruções

Escolha um membro do grupo:

* Crie uma pasta `fig` dentro da sua pasta do repositório
* Modifique o seu programa para fazer um gráfico com a lista original. No eixo
  x do gráfico, coloque o índice (posição na lista). No eixo y, coloque os
  valores da lista. Faça o gráfico com bolas pretas. Coloque títulos
  apropriados nos eixos.
* A figura deve ser salva na pasta `fig` como `bubble-inicio.png`
* Faça um gráfico da lista final (ordenada) com as mesmas características do
  gráfico anterior.
* Salve a figura na pasta `fig` como `bubble-fim.png`

Troque o membro do grupo:

* Modifique o programa para fazer um gráfico da lista como o descrito acima
  cada vez que houver uma troca
* Salve essas figuras como `bubble-troca-1.png`, `bubble-troca-2.png`, etc na
  pasta `fig`
* **Note que os gráficos começam com 1.**

Troque o membro do grupo:

* Modifique o programa para gerar um gráfico da lista a cada iteração do
  algoritmo. Ou seja, para todos os valores de `i` e `j`, havendo troca ou não.
* Nesses gráficos, o elemento `i` da vez deve ser uma bola vermelha e o
  elemento `j` deve ser uma bola azul.
* Salve as figuras como `bubble-it-1.png`, `bubble-it-2.png`, etc.

### Resultado esperado

Quando executado, seu programa deve imprimir algo parecido com:

    Lista original: [11, 18, 3, 1, 16, 12, 6, 19, 5, 0, 14, 4, 17, 9, 13, 7, 10, 15, 2, 8]
    Lista em ordem crescente: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19]
    Cinco maiores valores: [19, 18, 17, 16, 15]
    Cinco menores valores: [0, 1, 2, 3, 4]

Além disso, deve produzir figuras parecidas com:

![Exemplo de figuras](https://raw.githubusercontent.com/leouieda/mat-esp-python-intro/master/images/exemplo-figuras.png)

## Tarefa 3

### Leitura recomendada

* http://software-carpentry.org/v4/python/lists.html
* http://software-carpentry.org/v4/python/io.html

### Conceitos aplicados

### Instruções

Ler a lista de um arquivo.

**Dar arquivos para eles lerem**.

Primeiro de arquivo `.txt` com um número por linha.
Depois de um arquivo números separados por espaços em múltiplas linhas.
Depois de um arquivo CSV múltiplas linhas.

### Resultado esperado



## Finalizando

Faça um Pull Request.


## License

<a rel="license" href="http://creativecommons.org/licenses/by/4.0/"><img alt="Creative Commons License" style="border-width:0" src="https://i.creativecommons.org/l/by/4.0/88x31.png" /></a><br /><span xmlns:dct="http://purl.org/dc/terms/" href="http://purl.org/dc/dcmitype/Text" property="dct:title" rel="dct:type">"Material didático da disciplina Matemática Especial"</span>
by <a xmlns:cc="http://creativecommons.org/ns#" href="http://www.leouieda.com/" property="cc:attributionName" rel="cc:attributionURL">Leonardo Uieda</a> is licensed under a
<a rel="license" href="http://creativecommons.org/licenses/by/4.0/">Creative Commons Attribution 4.0 International License</a>.
