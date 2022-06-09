

# This file was *autogenerated* from the file ECDSA.sage
from sage.all_cmdline import *   # import sage library

_sage_const_16 = Integer(16); _sage_const_271 = Integer(271); _sage_const_0 = Integer(0); _sage_const_7 = Integer(7); _sage_const_1 = Integer(1); _sage_const_201 = Integer(201); _sage_const_247 = Integer(247); _sage_const_7259609 = Integer(7259609); _sage_const_11 = Integer(11); _sage_const_135 = Integer(135)
import random
import hashlib

def hashInt(x):
    h = hashlib.sha256(str(x).encode('utf-8')).hexdigest()
    return int(h, _sage_const_16 )

class ECDSA:
    def __init__(self):
        #criando a Curva        
        self.q = _sage_const_271 
        F = Zmod(self.q)
        self.E3 = EllipticCurve(F, [_sage_const_0 ,_sage_const_0 ,_sage_const_0 ,-_sage_const_7 , _sage_const_0 ])
        
        #usado para as operações modulo n 
        self.n = -_sage_const_1 
        
    def keygen(self, nUSP):
        #Criando o ponto gerador
        P = self.E3(_sage_const_201 , _sage_const_247 ) 
        #n é a ordem do ponto P (que é 136)
        self.n = P.order()

        nUSP = _sage_const_7259609  % self.n
        while nUSP == _sage_const_0 : 
            nUSP = (nUSP + _sage_const_1 ) % self.n

        Q = P*nUSP

        return (nUSP, (Q, P))

    def Assinatura(self, x, SK, PK):
        (Q, P) = PK
        s = Integer(SK)
        
        k = _sage_const_0          
        while k == _sage_const_0 : 
            try: 
                #Escolhendo k 
                k = random.randint(_sage_const_1 , self.n - _sage_const_1 )
                
                # calculando 
                R = k*P

                x1, _ = R.xy()
                
                r = Integer(x1)
                
                if _sage_const_0  < r < self.n:  
                    kInv = pow(k, -_sage_const_1 , self.n)
                    
                    a = (kInv*(hashInt(x) + r*s)) % self.n 
                    
                    #verificando se existe a inversa de a
                    if gcd(a, self.n) != _sage_const_1 : 
                        k = _sage_const_0                     
                else: 
                    k = _sage_const_0  
            except: 
                k = _sage_const_0  
        
        return (r, a)

    def verificacao(self,x, r, a, PK):   
        try: 
            (Q, P) = PK
            #calculando a inversa de a
            w = pow(a, -_sage_const_1 , self.n)
            
            #calculando u1 e u2
            u1 = (hashInt(x)*w) % self.n
            u2 = (r*w) % self.n
            
            #calculando a soma dos pontos
            S = Integer(u1)*P + Integer(u2)*Q

            x1, _ = S.xy()

            x1 = Integer(x1) 

            return _sage_const_0  < x1 < self.n and x1 == r
        
        except: 
            
            return False

signature = ECDSA()

(sk, pk) = signature.keygen(_sage_const_7259609 )

#Cases True 
x = _sage_const_11 
for m in range(_sage_const_1 , _sage_const_135 ):
    (r, a) = signature.Assinatura(m, sk, pk)
    ans = signature.verificacao(m, r, a, pk)
    print(">", m, ans)
    
#Cases False 
x = _sage_const_11 
for m in range(_sage_const_1 , _sage_const_135 ):
    (r, a) = signature.Assinatura(m, sk, pk)
    ans = signature.verificacao(m + _sage_const_1 , r, a, pk)
    print(">", m, ans)

