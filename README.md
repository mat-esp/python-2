# Python 2: condições e repetindo ações

Parte do curso
[Matemática Especial I](https://github.com/mat-esp/about)
da [UERJ](http://www.uerj.br/).

Ministrado por [Leonardo Uieda](http://www.leouieda.com/).


## Objetivos

* Aprender como repetir ações usando o comando `for`
* Aprender como executar ações diferentes dependendo de condições
  estabelecidas


## Leitura recomendada

Vamos seguir de perto o material
[Programming with Python](http://swcarpentry.github.io/python-novice-inflammation/)
e
[Plotting and programming in Python](http://swcarpentry.github.io/python-novice-gapminder/)
do Software Carpentry.
Farei algumas modificações para ser mais voltado para o tipo de dados que
costumamos encontrar nas geociências.

Uma ótima referência para aprender a usar o numpy e matplotlib é o
[Scipy Lectures](http://www.scipy-lectures.org/).


## Tarefa

Utilize o link enviado para a [lista de
emails](https://github.com/mat-esp/about#informa%C3%A7%C3%B5es) para criar um
repositório para seu grupo ou se juntar a um grupo já criado.
Anote o link para o repositório criado para seu grupo. Vocês precisarão desse
link.

Clone o repositório do seu grupo para seu computador. Não se esqueça de
configurar o git para um dos membros do grupo (`git config --global user.name
"Fulado de Tal"` e `git config --global user.email fulado@gmail.com`).

Vamos continuar com os dados de temperatura média que utilizamos na aula
anterior mas dessa vez teremos vários arquivos, um para cada cidade.
Os dados estão na pasta `dados`
desse repositório e foram baixados do site
[Berkeley Earth](http://berkeleyearth.org/):
por exemplo,
http://berkeleyearth.lbl.gov/locations/23.31S-42.82W

**IMPORTANTE**: tenha em mente o [checklist de
correção](https://github.com/mat-esp/about/blob/master/ISSUE_TEMPLATE.md#checklist-de-avalia%C3%A7%C3%A3o-do-professor)
quando fizer a tarefa. Não perca pontos de bobeira.
O site [pep8.org](http://pep8.org/) é uma boa referência para como escrever
código Python bem formatado.

Siga as instruções abaixo. Não se esqueça de fazer os commits. De preferência,
alterne a pessoa que está fazendo os commits.

1. Adicione no repositório um arquivo `alunos.txt` com os nomes completos de
   cada membro do grupo e seus nomes de usuário no github.com
2. Crie um Jupyter notebook chamado `python2.ipynb`. Todos os passos abaixo
   devem ser feitos nesse notebook. Use as células de texto do notebook para
   descrever o que você quis fazer com cada bloco de código.
3. Faça gráficos da anomalia de temperatura anual para cada arquivo da pasta
   `dados` referente a uma cidade (não o do Brasil todo). Você deve usar
   obrigatoriamente o comando `for`. Os gráficos devem ser salvos com o mesmo
   nome do arquivo mas com `.png` no lugar do `.txt`: ex.
   `0.80S-49.02W-TAVG-Trend.png`.

**BÔNUS**: Adicione no em cada gráfico a anomalia de 10 anos e o intervalo de
+- duas incertezas (95% uncertainty range) como nas figuras do site.


## Entrega das soluções

A solução de cada prática será um repositório no [Github](http://github.com/)
com o código feito pelos alunos.

A entrega das soluções será feita criando uma
[Issue](https://guides.github.com/features/issues/)
no repositório da disciplina
[mat-esp/about](https://github.com/mat-esp/about).
Utilize o link abaixo para ir direto para as Issues:

https://github.com/mat-esp/about/issues

Cada grupo deve criar uma Issue para entregar cada prática.
A issue deverá seguir o padrão abaixo:

* Título: Deve conter o nome da prática seguido dos nomes dos integrantes do
  grupo e a qual turma pertencem (caso haja mais de uma). Ex: "Prática
  Integração: Bilbo, John, Arthur - Turma 1"
* Corpo: Deve conter o link para o repositório do grupo (ex:
  `https://github.com/mat-esp-2016/integracao-sociedade-42`) e qualquer
  comentário que achar necessário (ex: problemas com os commits, erros que foram
  arrumados depois, dificuldades, etc).


## License

All content can be freely used and adapted under the terms of the
[Creative Commons Attribution 4.0 International License](http://creativecommons.org/licenses/by/4.0/).

![Creative Commons License](https://i.creativecommons.org/l/by/4.0/88x31.png)
