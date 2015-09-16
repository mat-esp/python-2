# Prática de introdução ao Python

## Objetivos

## Preparação

Faça um fork do repositório para sua conta no github.
Adicione os outros membros do grupo como colaboradores no projeto.
Pegue um clone para cada membro e configure o git para cada clone.

Comandos importantes:

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
* Imprimir para a tela: `print("Resultado do programa:", a)`
* Comentários: `# Linhas começando com '#' são comentários`
* Executar comandos de um arquivo com `$ python arquivo.py`

### Instruções

Crie uma pasta com os primeiros nomes do grupo: `aluno1-aluno2-aluno3` dentro
do repositório.
Coloque **todos** os arquivos que você fizer nessa pasta.
Colocar o bubble sort num arquivo .py e rodar com uma lista escrita a mão com
20 elementos.
**Dar lista para eles usarem**.
Ao final, o programa deve imprimir a lista organizada.
Outro aluno deve colocar comentários explicando cada linha do programa.
Outro aluno deve colocar fazer o programa imprimir ao final os 5 maiores e os 5
menores valores.

* **Não esqueça de fazer as alterações em seu clone pessoal.**
* **Use `git commit` com frequência.**

### Resultado esperado

## Tarefa 2

### Leitura recomendada

* http://scipy-lectures.github.io/intro/matplotlib/matplotlib.html
* http://matplotlib.org/gallery.html

### Conceitos aplicados

### Instruções

Faça um gráfico com o estado inicial da lista e um com o estado final.
Salve os gráficos como `bubble-inicio.jpg` e `bubble-fim.jpg`.
Salve todas as figuras em uma pasta `figs`.
Outro aluno faça um gráfico para cada vez que houver uma troca.
Salve os gráficos como `bubble-troca-1.jpg`, `bubble-troca-2.jpg` etc.
**Note que os gráficos começam com 1.**
Outro aluno faça um gráfico para cada iteração do algoritmo.
Salve como `bubble-it-1.jpg`, `bubble-it-2.jpg`, etc.
Nesses gráficos, o elemento `i` deve ser vermelho e o elemento `j` deve ser
azul.

### Resultado esperado

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
