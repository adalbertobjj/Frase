frase = input('Digite sua frase aqui: ')
invertida = ' '. join(palavra[::-1] for palavra in frase.split())
print("A frase é: {}".format(invertida))

