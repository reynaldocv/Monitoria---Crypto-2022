import random
import hashlib

def hashInt(x):
    h = hashlib.sha256(str(x).encode('utf-8')).hexdigest()
    return int(h, 16)

class ECDSA:
    def __init__(self):
        #criando a Curva        
        self.q = 271
        F = Zmod(self.q)
        self.E3 = EllipticCurve(F, [0,0,0,-7, 0])
        
        #usado para as operações modulo n 
        self.n = -1
        
    def keygen(self, nUSP):
        #Criando o ponto gerador
        P = self.E3(201, 247) 
        #n é a ordem do ponto P (que é 136)
        self.n = P.order()

        nUSP = 7259609 % self.n
        while nUSP == 0: 
            nUSP = (nUSP + 1) % self.n

        Q = P*nUSP

        return (nUSP, (Q, P))

    def Assinatura(self, x, SK, PK):
        (Q, P) = PK
        s = Integer(SK)
        
        k = 0         
        while k == 0: 
            try: 
                #Escolhendo k 
                k = random.randint(1, self.n - 1)
                
                # calculando 
                R = k*P

                x1, _ = R.xy()
                
                r = Integer(x1)
                
                if 0 < r < self.n:  
                    kInv = pow(k, -1, self.n)
                    
                    a = (kInv*(hashInt(x) + r*s)) % self.n 
                    
                    #verificando se existe a inversa de a
                    if gcd(a, self.n) != 1: 
                        k = 0                    
                else: 
                    k = 0 
            except: 
                k = 0 
        
        return (r, a)

    def verificacao(self,x, r, a, PK):   
        try: 
            (Q, P) = PK
            #calculando a inversa de a
            w = pow(a, -1, self.n)
            
            #calculando u1 e u2
            u1 = (hashInt(x)*w) % self.n
            u2 = (r*w) % self.n
            
            #calculando a soma dos pontos
            S = Integer(u1)*P + Integer(u2)*Q

            x1, _ = S.xy()

            x1 = Integer(x1) 

            return 0 < x1 < self.n and x1 == r
        
        except: 
            
            return False

signature = ECDSA()

(sk, pk) = signature.keygen(7259609)

#Cases True 
x = 11
for m in range(1, 135):
    (r, a) = signature.Assinatura(m, sk, pk)
    ans = signature.verificacao(m, r, a, pk)
    print(">", m, ans)
    
#Cases False 
x = 11
for m in range(1, 135):
    (r, a) = signature.Assinatura(m, sk, pk)
    ans = signature.verificacao(m + 1, r, a, pk)
    print(">", m, ans)
