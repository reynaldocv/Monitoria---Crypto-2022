
import hashlib

def autenticacao(mensagem, chave):
	m = mensagem.encode("utf-8")
	k = chave.encode("utf-8")
	
	# operação de concatenação de sequências de bytes
	
	c = m + k 
	
	return hashlib.sha512(c).hexdigest()

def representacao_binaria(h):
	binario = bin(int(h, 16))[2:]
	
	return '0'*(512 - len(binario)) + binario
	
chave = "chave"

binario1 = representacao_binaria(autenticacao("mensagem 1", chave))
binario2 = representacao_binaria(autenticacao("mensagem 2", chave))

def distancia_Hamming(binario1, binario2): 
	distancia = 0
	for i in range(512):
		if binario1[i] != binario2[i]:
			distancia = distancia + 1
			
	return distancia
	
print(distancia_Hamming(binario1, binario2))
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
