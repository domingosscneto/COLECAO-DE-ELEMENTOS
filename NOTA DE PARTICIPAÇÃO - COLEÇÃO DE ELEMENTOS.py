#Domingos Soares do Carmo Neto - TIA: 32032889
#Joao Pedro de Paula Oliveira do Amaral - TIA: 32049390

import sys

def adicionaFinal(coleção, qnt, elemento):
    if qnt < 100:
        coleção[qnt] = elemento
        qnt += 1
    print('Quantidade de elementos na coleção:', qnt)
    if qnt >= 100:
        print('Coleção com número máximo de elementos!')
    return qnt


def printVálidos(coleção,qnt) :
    i=0
    print('coleção:[',end=' ')
    while i < qnt:
        print(coleção[i],end=' ')
        i+=1
    print(']',end=' ')
    print()
    print('')


def adicionaPosição(coleção, qnt, posição, elemento):
    if qnt < 100 and posição <= qnt:
        coleção[posição + 1] = coleção[posição]
        coleção[posição] = elemento
        qnt +=1
    print('Quantidade de elementos na coleção:', qnt)
    if qnt >= 100:
        print('Coleção com número máximo de elementos!')
    if posição > qnt:
        print('Escolha uma posição válida!')
    return qnt


def removePosição(coleção, qnt, posição):
    if qnt > 0:
        if posição < qnt:
            del coleção[posição]
            qnt -=1
            coleção.append(0)
            print('Quantidade de elementos na coleção:', qnt)
        if posição >= qnt:
            print('Essa posição ainda não foi preenchida na sua coleção!')
    if qnt <= 0:
        print('A sua coleção está vazia!')
    return qnt


def removeElemento(coleção, qnt, elemento):
    if qnt > 0:
        if elemento in coleção:
            i = coleção.index(elemento)
            del coleção[i]
            del coleção[qnt-1]
            qnt -=1
            coleção.append(0)
            coleção.append(0)
            print('Quantidade de elementos na coleção:', qnt)
        else:
            print('O elemento digitado não está presente na coleção!')
    if qnt <= 0:
        print('A sua coleção está vazia!')
    return qnt


def removeElementos(coleção, qnt, elemento):
    if qnt > 0:
        if elemento in coleção:
            i = coleção.index(elemento)
            del coleção[i]
            del coleção[qnt - 1]
            qnt -= 1
            coleção.append(0)
            coleção.append(0)
        else:
            print('O elemento digitado não está presente na coleção!')
    if qnt <= 0:
        print('A sua coleção está vazia!')
    return qnt


def verificaElemento(coleção, elemento):
    if elemento in coleção:
        print(f'O elemento {elemento} está presente na coleção!')
    else:
        print(f'o elemento {elemento} não está presente na coleção!')
    return elemento


def main():
    coleção = [0 for x in range(100)]
    qnt = 0
    escolha = -1
    print('')
    print('1. Adicionar um elemento no final da coleção. ')
    print('2. Adicionar um elemento em uma posição da coleção.')
    print('3. Remover um elemento em uma posição na coleção.')
    print('4. Remover a primeira ocorrência do elemento na coleção.')
    print('5. Remover todas as ocorrências de um elemento na coleção.')
    print('6. Verificar se dado um elemento está contido na coleção.')
    print('7. Verificar se dado um valor existem dois elementos na coleção que somados é igual a um valor informado.')
    print('8. Mostrar o menu de opções.')
    print('9. Sair.')
    while escolha != 9:
        escolha = int(input('Escolha uma operação: '))
        print('')
        if escolha == 1:
            elemento = int(input('Digite o elemento que deseja adicionar no final da coleção: '))
            qnt = adicionaFinal(coleção, qnt, elemento)
        if escolha == 2:
            elemento = int(input('Digite o elemento que deseja adicionar na coleção: '))
            posição = int(input('Digite a posição que deseja adicionar o novo elemento: '))
            qnt = adicionaPosição(coleção, qnt, posição, elemento)
        if escolha == 3:
            posição = int(input('Digite a posição do elemento que deseja remover: '))
            qnt = removePosição(coleção, qnt, posição)
        if escolha == 4:
            elemento = int(input('Digite o elemento que deseja remover da coleção (apenas a primeira ocorrência do elemento será removida): '))
            qnt = removeElemento(coleção, qnt, elemento)
        if escolha == 5:
            elemento = int(input('Digite o elemento que deseja remover da coleção (todas as ocorrências desse elemento serão removidas): '))
            C = coleção.count(elemento)
            for x in range(C):
                qnt = removeElementos(coleção, qnt, elemento)
            print('Quantidade de elementos na coleção:', qnt)
        if escolha == 6:
            elemento = int(input('Digite o elemento que deseja verificar se está presente na coleção: '))
            verificaElemento(coleção, elemento)
        if escolha == 8:
            print('')
            print('1. Adicionar um elemento no final da coleção. ')
            print('2. Adicionar um elemento em uma posição da coleção.')
            print('3. Remover um elemento em uma posição na coleção.')
            print('4. Remover a primeira ocorrência do elemento na coleção.')
            print('5. Remover todas as ocorrências de um elemento na coleção.')
            print('6. Verificar se dado um elemento está contido na coleção.')
            print('7. Verificar se dado um valor existem dois elementos na coleção que somados é igual a um valor informado.')
            print('8. Mostrar o menu de opções.')
            print('9. Sair.')
        if 1 <= escolha and escolha <= 8:
            printVálidos(coleção, qnt)
        if escolha == 9:
            sys.exit('fim!')

main()