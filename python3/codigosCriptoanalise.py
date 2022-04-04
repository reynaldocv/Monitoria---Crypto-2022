
from codigos import codigos
	
cesar = codigos()

file = open("mensagem.txt","r")

mensagem = file.read()
mensagem = mensagem.lower()

chave = 13

criptograma = cesar.encriptacao(mensagem, chave)

print(criptograma[: 500])

contador = {}

caracterMaisComum = "$"

maxFrequencia = 0 

for caracter in criptograma:

	if caracter.isalpha():
		if caracter in contador:			
			contador[caracter] = contador[caracter] + 1
		else:
			contador[caracter] = 1
		
		if maxFrequencia < contador[caracter]:		
			maxFrequencia = contador[caracter]
			caracterMaisComum = caracter

chaveCalculada = (26 + ord(caracterMaisComum) - ord("e")) % 26			

print("-")

print(chave, chaveCalculada, chave == chaveCalculada)
	
	
	
	
	
	

	

		

