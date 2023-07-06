# 1 - Reverter a ordem das palavras na frase, mantendo a ordem das palavras
def reverso(frase):
    palavra = frase.split()
    frase_reversa = ' '.join(reversed(palavra))
    return frase_reversa

entrada_reverter = "Hello, World! OpenAl is amazing."
saida_reverter = reverso(entrada_reverter)
print("Reverter: ", saida_reverter)

# 2 - Remover todos os caracteres duplicados da string
def remover(string):
    unicos = list(dict.fromkeys(string))
    return ''.join(unicos)

entrada_remover = "Hello, World!"
saida_remover = remover(entrada_remover)
print("Remover : ", saida_remover)

# 3 - Encontrar a substring palindrômica mais longa na string
def substring(string):
    max_length = 0
    maior_substring = ""

    for i in range(len(string)):
        for j in range(i+1, len(string)+1):
            substring = string[i:j]
            if substring == substring[::-1] and len(substring) > max_length:
                max_length = len(substring)
                maior_substring = substring 
    
    return maior_substring

entrada_substring = "String Palindromo definição: Uma palavra é dita palíndroma quando possui o mesmo significado se lida da esquerda para a direita ou da direita para a esquerda"
saida_substring = substring(entrada_substring)
print("Substring: ", saida_substring)

# 4 - Colocar em maíuscula a primeira letra de cada frase na string
def primeira_maiuscula(input_string):
    maiuscula = []
    frase = input_string.split(". ")
    for sentence in frase:
        letra_maiuscula = sentence.capitalize()
        maiuscula.append(letra_maiuscula)
    output_string = ". ".join(maiuscula)
    return output_string

entrada_maiuscula = "hello. how are you? I'm fine, thank you."
saida_maiuscula = primeira_maiuscula(entrada_maiuscula)
print("Maiúscula: ", saida_maiuscula)

# 5 - Verificar se a string é um anagrama de um palíndromo: 
from collections import Counter

def anagrama_palindromo(frase):
    frase_limpa = ''.join(letra.lower() for letra in frase if letra.isalpha())
    contagem_letras = Counter(frase_limpa)
    contagem_impares = 0

    for contagem in contagem_letras.values():
        if contagem % 2 != 0:
            contagem_impares += 1
            if contagem_impares > 1:
                return False

    return True

entrada_frase = "racecar"
saida_resultado = anagrama_palindromo(entrada_frase)
print("Anagrama: ", saida_resultado)

input("Aperte ENTER para fechar")
