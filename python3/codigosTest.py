
from codigos import codigos 
	
cesar = codigos()

mensagem = """cryptography, or cryptology is the practice and study of techniques for secure
communication in the presence of adversarial behavior. More generally, cryptography
is about constructing and analyzing protocols that prevent third parties or the public
from reading private messages; various aspects in information security such as data..."""

chave = 3

print(mensagem)
print("-")

criptograma = cesar.encriptacao(mensagem, chave)
print(criptograma)
print("-")

mensagem = cesar.decriptacao(criptograma, chave)
print(mensagem)
print("-")


