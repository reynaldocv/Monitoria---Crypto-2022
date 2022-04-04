
from vigenere import vigenere
	
criptossistema = vigenere()

mensagem = """cryptography, or cryptology is the practice and study of techniques for secure
communication in the presence of adversarial behavior. More generally, cryptography
is about constructing and analyzing protocols that prevent third parties or the public
from reading private messages; various aspects in information security such as data..."""

chave = "chave"

print(mensagem)
print("-")

criptograma = criptossistema.encriptacao(mensagem, chave)
print(criptograma)
print("-")

mensagem = criptossistema.decriptacao(criptograma, chave)
print(mensagem)
print("-")


