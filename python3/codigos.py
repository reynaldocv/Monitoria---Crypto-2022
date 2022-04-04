
class codigos:

	def encriptacao(self, mensagem, chave):
		criptograma = ""
		
		for caracter in mensagem: 
			if caracter.isalpha():
				posicao = ord(caracter) - ord("a")
				posicao = (posicao + chave) % 26
				criptograma += chr(posicao + ord("a"))
			else:
				criptograma += caracter
			
		return criptograma
		
	def decriptacao(self, criptograma, chave):		
		return self.encriptacao(criptograma, 26 - chave)
		

