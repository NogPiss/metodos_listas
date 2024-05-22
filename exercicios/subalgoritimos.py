#1. Fazer um procedimento chamado ‘preenche_lista(l)’ que preencha uma lista passada por parâmetro.
def preenche_lista(lista: list) -> None:
    lista = [1,2,3,4,5]
#2. Fazer um procedimento chamado ‘exibe_lista(l)’ que exiba os elementos da lista passada por parâmetro..
def exibe_lista(lista: list) -> None:
    print(lista)
#3. Sabemos que a função len() do Python retorna a quantidade de elementos de uma lista. Faça uma função chamada ‘conta_elementos(l)’ que tenha o mesmo efeito.
def conta_elementos(lista: list) -> int:
    qtd = len(lista)
    return qtd
#4. Sabemos que a função index() do Python retorna o índice do elemento passado por parâmetro. Faça uma função parecida chamada ‘retorna_indice(elemento)’ com a melhoria de retornar -1 caso o elemento não seja encontrado..
def retorna_indice(elemento, lista: list) -> int:
    try:
        indice = lista.index(elemento)
        return indice
    except ValueError:
        return -1
    
    
#5. Sabemos que a função count() do Python retorna a quantidade de um elemento especifico. Faça uma função chamada ‘busca(l,elemento)’ que tenha o mesmo efeito.
def busca(l: list, elemento: int) -> int:
    qtd = l.count(elemento)
    return qtd

#6. Fazer uma função chamada ‘conta_inteiro(l)’ que conte quantos elementos inteiros existem em uma lista.
#def conta_interio(l: list):
 #   for i in range(len(l)):
  #      if l[i] =