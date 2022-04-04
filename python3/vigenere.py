
class vigenere:

	def encriptacao(self, mensagem, chave):
		criptograma = ""

		n = len(chave)
		i = 0 
		
		for caracter in mensagem: 
			if caracter.isalpha():
				posicao      = ord(caracter) - ord("a")				
				deslocamento = ord(chave[i]) - ord("a")
				
				posicao = (posicao + deslocamento) % 26
				
				criptograma += chr(posicao + ord("a"))
				
				i = i + 1
				
				if i == n:
					i = 0 
				
			else:
				criptograma += caracter
			
		return criptograma
		
	def decriptacao(self, criptograma, chave):
		mensagem = ""

		n = len(chave)
		i = 0 
		
		for caracter in criptograma: 
			if caracter.isalpha():
				posicao      = ord(caracter) - ord("a")				
				deslocamento = ord(chave[i]) - ord("a")
				
				posicao = (posicao - deslocamento) % 26
				
				mensagem += chr(posicao + ord("a"))
				
				i = i + 1
				
				if i == n:
					i = 0 
				
			else:
				mensagem += caracter
			
		return mensagem


