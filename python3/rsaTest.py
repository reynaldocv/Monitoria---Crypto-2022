
from rsa import rsa
	
criptossistema = rsa()

pk, sk = rsa.geracao(512)

print("sk", sk)

print("-")

print("pk", pk)

print("-")

mensagem = "Olá mundo!!!"
print(mensagem)
print("-")

criptograma = criptossistema.encriptacao(mensagem, pk)
print(criptograma)
print("-")

mensagem = criptossistema.decriptacao(criptograma, sk)
print(mensagem)
print("-")



