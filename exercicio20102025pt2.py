lista_numeros = [1,9,3,7,5]

# Questão 6

print(f"tamanho da lista: {(len(lista_numeros))}")

# Questão 7

print(f"Soma dos números da lista: {sum(lista_numeros)}")

# Questão 8

print(f"Numeros em ordem crescente: {sorted(lista_numeros)}")

# Questão 9

print(f"Números em ordem decrescente: {sorted(lista_numeros, reverse=True)}")

# Questão 10

lista1 = [1,2,3]
lista2 = [4,5,6]

lista_mesclada = lista1 + lista2
print(f"Lista mesclada: {lista_mesclada}")

# Questão 11

entrada_usuario = int(input("Digite um número para verificar se está na lista: "))
if entrada_usuario in lista_numeros:
    print(f"O número {entrada_usuario} está na lista.")
else:
    print(f"O número {entrada_usuario} não está na lista.")