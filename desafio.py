# 1 - Reverter a ordem das palavras na frase, mantendo a ordem das palavras
def reverso(frase):
    palavra = frase.split()
    frase_reversa = ' '.join(reversed(palavra))
    return frase_reversa

input_sentence = "Hello, World! OpenAl is amazing."
output_sentence = reverso(input_sentence)
print(output_sentence)
