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
