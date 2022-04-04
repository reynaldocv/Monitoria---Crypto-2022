
from Crypto.Util import number
from math import gcd

class rsa:
	def geracao(n, e = 2**16 + 1):
		p = number.getPrime(n)
		q = number.getPrime(n)

		N = p*q
		phi = (p - 1)*(q - 1)
		
		if gcd(e, phi) == 1: 
			d = pow(e, -1, phi)
			
			pk = (e, N)
			sk = (d, N)
		
			return pk, sk 
		
	def encriptacao(self, mensagem, pk):
		binario = self.encode(mensagem)
		(e, N) = pk
		
		return pow(binario, e, N)
		
	def decriptacao(self, criptograma, sk):		
		(d, N) = sk
		binario = pow(criptograma, d, N)
		
		return self.decode(binario)
		
	def encode(self, mensagem): 
		binario = 0
		base = 1 
		for letra in mensagem: 
			binario += base*ord(letra)
			base *= 256
			
		return binario 
	
	def decode(self, binario):
		mensagem = ""
		while binario > 0: 
			letra = chr(binario % 256)
			binario = binario//256
			
			mensagem = mensagem + letra
			
		return mensagem
			
	
	
	
		
		

		

