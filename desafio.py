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
print("Remover : ",saida_remover)

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


