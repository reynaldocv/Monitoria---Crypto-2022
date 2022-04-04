
import hashlib

mensagem1 = "este e um test"

hash1 = hashlib.sha512(mensagem1.encode("utf-8"))

print(hash1.digest())

print("-")

print(hash1.hexdigest())


