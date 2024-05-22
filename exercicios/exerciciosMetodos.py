import os
os.system("cls")

import subalgoritimos

lista = [1,2,3,4,5,6,7,8,9]
'''print(lista_teste)'''

escolha = int(input("insira o numero do exercicio desejado(1-6): "))

match escolha:
    case 1: 
        subalgoritimos.preenche_lista(lista)
    case 2: 
        subalgoritimos.exibe_lista(lista)
    case 3: 
        subalgoritimos.conta_elementos(lista)
    case 4: 
        elemento = int(input("Escolha o numero que vc deseja procurar na lista: "))
        print(subalgoritimos.retorna_indice(elemento, lista))
    case 5:
        elemento = int(input("escolha um elemnto que você deseja contar dentro da lista: "))
        print(subalgoritimos.busca(lista, elemento))
    #case 6:
        