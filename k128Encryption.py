# # iterations = 12
R = 12

# KEYGEN

constant1 = int("9e3779b97f4a7151", 16)
constant2 = int("8aed2a6bb7e15162", 16)
constant3 = int("7c159e3779b97f4a", 16)

def aSum(num1, num2):
    return (num1 + num2) % (2**64)

def aRot(num1, k):    
    k %= 64
    
    if k == 0: 
        return num1 
    else: 
        numA = (num1 << k) % (2**64)        
        numB = (num1 >> (64 - k))
        return numA + numB

def keygen(key):
    L = [0 for _ in range(4*R + 3)]
    K = [0 for _ in range(4*R + 3)]
    
    L[0] = key >> 64
    L[1] = key % (2**64)
    
    for j in range(2, 4*R + 3):
        L[j] = aSum(L[j - 1], constant1)
        
    K[0] = constant2
    
    for j in range(1, 4*R + 3):
        K[j] = aSum(K[j - 1], constant3)
        
    i, j, A, B = 0, 0, 0, 0
    
    for s in range(1, 4*R + 4):
        K[i] = aRot(aSum(B,aSum(A, K[i])), 3)
        A = K[i]
        i += 1 
        
        L[j] = aRot(aSum(A, aSum(B, L[j])), aSum(A, B))
        B = L[j]
        j += 1
    
    return K[1:]        

# Cryptosystem k 128

def inverse(num):
    return (2**64) - num

expo = [0 for i in range(256)]
loga = [0 for i in range(256)]
for i in range(256):
    expo[i] = pow(45, i, 257) % 256
    loga[expo[i]] = i 
    
def ponto(num1, num2):
    arr1 = []
    for i in range(8):
        arr1.append(num1 % 256)
        num1 //= 256
    
    arr2 = []
    for i in range(8):
        arr2.append(num2 % 256)
        num2 //= 256
        
    ans = 0 
    p = 1
    for i in range(8):
        ans += expo[arr1[i] ^ arr2[i]]*p
        p*= 256
        
    return ans 
    
def iteration1(Xa, Xb, kA, kB):
    return ponto(Xa, kA), aSum(Xb, kB)

def iteration2(Xe, Xf, kE, kF):
    Y1 = Xe^Xf
    Y2 = ponto(aSum(ponto(kE, Y1), Y1), kF)
    Z = aSum(ponto(kE, Y1), Y2)
    
    return Xe^Z, Xf^Z

def lastIteration(Xe, Xf, kA, kB):
    return ponto(Xf, kA), aSum(Xe, kB)
    
# Encryption

def Encription(num, password):
    keys = keygen(password)
    
    X1 = num % (2**64)    
    X2 = num >> 64
    print("number:", num)
    print("LSB: ", X1, "MSB:", X2)
    
    for ith in range(12):
        X1, X2 = iteration1(X1, X2, keys[4*ith + 0], keys[4*ith + 1])
        #print(X1, X2)
    
        X1, X2 = iteration2(X1, X2, keys[4*ith + 2], keys[4*ith + 3])
        print("round (", ith + 1, ")" , X1, X2)
    
        
    X1, X2 = lastIteration(X1, X2, keys[48], keys[49])
    print("last round ", X1, X2)
    
    
    return X1 + X2*2**64
    
#

def toInt(string):    
    ans = 0 
    
    p = 1
    for i in range(16):
        ans += ord(string[i])*p
        p *= 256
        
    return ans 

def toString(num):
    ans = ""
    
    for i in range(16):
        ans += chr(num % 256)
        num //= 256
        
    return ans 
    
# test

plainText = "AAAAAAAABBBBBBBB"
password  = "FFFFFFFF11111111"

plainTextInt = toInt(plainText)
passwordInt  = toInt(password)

keys = keygen(passwordInt)

for (ith, key) in enumerate(keys): 
    print("key", ith + 1, keys[ith])    
print()

criptograma = Encription(plainTextInt, passwordInt)

print("criptograma :", criptograma)
print()
print("ENC(",toString(plainTextInt),",", toString(passwordInt),") = ", toString(criptograma))
