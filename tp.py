#exercice 1

def puissance(x,n):
    if n==1:
        return x
    if n%2 ==0:
        return puissance(x**2,n//2)
    else:
        return  x*puissance(x**2,(n-1)//2)
print(puissance(2,5))  



#exercice 3

def taille_liste(L):
    if L == []:  
        return 0
    else:
        return 1 + taille_liste(L[1:])  


def sum_liste(L):
    if L == []:  
        return 0
    else:
        return L[0] + sum_liste(L[1:])
def aff_liste_inv(L):
    if L == []:
        return
    else:
        aff_liste_inv(L[1:])  
        print(L[0])  
L = [10, 20, 30]

print("Taille liste :", taille_liste(L))  # ➜ 3
print("Somme liste :", sum_liste(L))      # ➜ 60
print("Affichage inversé :")
aff_liste_inv(L)


#EXERCICE 4


def strcpm(ch1:str,ch2:str)-> int:
        if ch1>ch2 or ch1<ch2:
             return 1
        else :
            return 0
       

def strcpy(src: str, dest: str = "") -> str:
    if src == "":
        return dest
    return strcpy(src[1:], dest + src[0])

       
def taille_chaine(l: str) -> int:
    if l == "":
        return 0
    return 1 + taille_chaine(l[1:])

def supprimer_le_premiere(l: str, m: str) -> str:
    if l == "":
        return ""
    if l[0] == m:
        return l[1:]
    return l[0] + supprimer_le_premiere(l[1:], m)

def anagramme(ch1: str, ch2: str) -> bool:
    if ch1 == "" and ch2 == "":
        return True
    if taille_chaine(ch1) != taille_chaine(ch2):
        return False
    if ch1[0] not in ch2:
        return False
    nouve_ch1 = ch1[1:]
    nouve_ch2 = supprimer_le_premiere(ch2, ch1[0])
    return anagramme(nouve_ch1, nouve_ch2)

print(strcpy("photo"))              
print(strcpm("chat", "chien"))    
print(strcpm("manar", "manal"))    
print(strcpm("hajar", "hajar"))      
print(anagramme("algorithme", "logarithme"))  
print(anagramme("chien", "nich"))      
     
#EXERCICE 5 
#exercice 1

def factorielle(n):

    if n < 0:
        return False # Retourne false si n est négatif
    elif n == 0:
        return 1    # Par convention, 0! = 1
    else:
        resultat = 1
        for i in range(1, n + 1):  # De 1 à n inclus
            resultat *= i
        return resultat

print(factorielle(5))


#exercice  2

def divise(a,b):
    if a==0:
        return False
    elif b==0:
        return 0
    else:
            return b//a
print(divise(4,9))


#exercice 3

def divis(a,b):
    if b==0:
        return False
    else:
        q=0
        r=0
        divis(a,b,q,r)
        print("q=",q,"r=",r)

#exercice 5


def division_entiere(a, b):
    q = a // b
    r = a % b
    return q, r

a = int(input("Entrez l'entier A : "))
b = int(input("Entrez l'entier B : "))

q, r = division_entiere(a, b)

print("Le quotient :", q, "et le reste :", r)