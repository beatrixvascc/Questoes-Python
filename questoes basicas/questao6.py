#Escreva um programa que leia duas strings. Verifique se a segunda ocorre dentro da primeira
#e imprima a posição de início.
#1ª string: AABBEFAATT
#2ª string: BE
#Resultado: BE encontrado na posição 3 de AABBEFAATT


string1 = input('digite uma string: ')
string2 = input('digite uma string: ')
if string2 in string1:
    posicao = string1.find(string2)
    print(posicao)