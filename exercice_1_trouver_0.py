from math import *

### Deux méthodes pour trouver x tel que f(x) = 0 (à compléter) ###

def dichotomie ( fonction, a, b ) :
    i = 0
    while ( a != b and i < 100 ) :
        i = i+1
        c = ( a + b ) / 2
        if ( fonction ( a ) * fonction ( c ) <= 0 ) :
            b = c
        else :
            a = c
        
    return c
    
def secante ( fonction, xn, b ) :
    i = 0
    while ( fonction(xn) != 0 and i < 100 ) :
        i = i+1
        num = b - xn
        denom = fonction(b)-fonction(xn)
        xn = xn - (num/denom)*fonction(xn)
    
    return xn
    
### Choix de la fonction à tester (décommenter celle voulue) ###

#trouver_0 = dichotomie
trouver_0 = secante
    
### Les fonctions à tester (ne pas modifier !) ###
print()

# Identité
def identite ( x ) :
    return x
    
print ( "f(x) = x" ) 
print ( "[-1 ; 1]" ) 
x = trouver_0( identite, -1, 1 )
print ( "x =", x )
print ( "f(x) =", identite(x) )
print()

# Sinus
def sinus ( x ) :
    return sin(x)
    
print ( "f(x) = sin(x)" ) 
print ( "[-PI/2 ; PI/2]" ) 
x = trouver_0( sinus, -pi/2, pi/2 )
print ( "x =", x )
print ( "f(x) =", sinus(x) )
print()
  
# Cosinus  
def cosinus ( x ) :
    return cos(x)
    
print ( "f(x) = cos(x)" ) 
print ( "[0 ; PI]" ) 
x = trouver_0( cosinus, 0, pi )
print ( "x =", x )
print ( "f(x) =", cosinus(x) )
print()

# Tangente
def tangente ( x ) :
    return tan(x)
    
print ( "f(x) = tan(x)" ) 
print ( "[-PI/2 ; PI/2]" ) 
x = trouver_0( tan, -pi/2, pi/2 )
print ( "x =", x )
print ( "f(x) =", tangente(x) )
print()

# Linéaire
def lineaire ( x ) :
    return -2*x + 5
    
print ( "f(x) = -2x + 5" ) 
print ( "[2 ; 3]" ) 
x = trouver_0( lineaire, 2, 3 )
print ( "x =", x )
print ( "f(x) =", lineaire(x) )
print()

# Quadratique 
def quadratique ( x ) :
    return -3*x*x + 5*x - 1
    
print ( "f(x) = -3*x^2 + 5x -1" ) 
print ( "[1 ; 2]" ) 
x = trouver_0( quadratique, 1, 2 )
print ( "x =", x )
print ( "f(x) =", quadratique(x) )
print()


# Cubique
def cubique ( x ) :
    return x*x*x + 2*x*x - 6*x + 3
    
print ( "f(x) = x^3 + 2x^2 - 6x + 3 " ) 
print ( "[-5 ; -3]" ) 
x = trouver_0( cubique, -5, -3 )
print ( "x =", x )
print ( "f(x) =", cubique(x) )
print()