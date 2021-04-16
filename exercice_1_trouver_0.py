from math import *

### Variables globales ###
epsilon = 10**(-15)
pas = 0.1

### Deux fonctions pour trouver x tel que f(x) = 0 ###
### et une fonction pour trouver tous les zéros    ###
### (à compléter)                                  ###
def dichotomie ( fonction, a, b ) :
    return 0
    
def secante ( fonction, xn, b ) :
    return 0
 
def multiple ( fonction, u, v, pas ) :
    return []
    
### Choix de la fonction à tester (décommenter celle voulue) ###

trouver_0 = dichotomie
#trouver_0 = secante
#trouver_0 = multiple
    
### Les fonctions à tester (ne pas modifier !) ###

# Identité
def identite ( x ) :
    if ( isinstance ( x, float ) or isinstance ( x, int ) ) :
        return x
    else : 
        res = []
        for i in range ( len ( x ) ) :
            res.append ( x[i] )
        return res
    
# Sinus
def sinus ( x ) :
    if ( isinstance ( x, float ) or isinstance ( x, int ) ) :
        return sin(x)
    else : 
        res = []
        for i in range ( len ( x ) ) :
            res.append ( sin( x[i] ) )
        return res
    
# Cosinus  
def cosinus ( x ) :
    if ( isinstance ( x, float ) or isinstance ( x, int ) ) :
        return cos(x)
    else : 
        res = []
        for i in range ( len ( x ) ) :
            res.append ( cos( x[i] ) )
        return res
    
# Tangente
def tangente ( x ) :
    if ( isinstance ( x, float ) or isinstance ( x, int ) ) :
        return tan(x)
    else : 
        res = []
        for i in range ( len ( x ) ) :
            res.append ( tan( x[i] ) )
        return res
    
# Linéaire
def lineaire ( x ) :
    if ( isinstance ( x, float ) or isinstance ( x, int ) ) :
        return -2*x + 5
    else : 
        res = []
        for i in range ( len ( x ) ) :
            res.append ( lineaire( x[i] ) )
        return res
    
# Quadratique 
def quadratique ( x ) :
    if ( isinstance ( x, float ) or isinstance ( x, int ) ) :
        return -3*x*x + 5*x - 1
    else : 
        res = []
        for i in range ( len ( x ) ) :
            res.append ( quadratique( x[i] ) )
        return res
    
# Cubique
def cubique ( x ) :
    if ( isinstance ( x, float ) or isinstance ( x, int ) ) :
        return x*x*x + 2*x*x - 6*x + 3
    else : 
        res = []
        for i in range ( len ( x ) ) :
            res.append ( cubique( x[i] ) )
        return res

### L'affichage (ne pas modifier !) ###
print()

if ( trouver_0 == dichotomie ) :
    print ( "*** Dichotomie ***\n" )
elif ( trouver_0 == secante ) :
    print ( "*** Sécante ***\n" )
else :
    print ( "*** Recherche multiple ***\n" )
   
print ( "f(x) = x" ) 
if ( trouver_0 != multiple ) :
    print ( "[-1 ; 1]" ) 
    x = trouver_0( identite, -1, 1 )
else :
    print ( "[-5 ; 5[" ) 
    x = trouver_0( identite, -5, 5, pas )
print ( "x =", x )
print ( "f(x) =", identite(x) )
print()
  
print ( "f(x) = sin(x)" ) 
if ( trouver_0 != multiple ) :
    print ( "[-PI/2 ; PI/2]" ) 
    x = trouver_0( sinus, -pi/2, pi/2 )
else :
    print ( "[-5 ; 5[" ) 
    x = trouver_0( sinus, -5, 5, pas )
print ( "x =", x )
print ( "f(x) =", sinus(x) )
print()
    
print ( "f(x) = cos(x)" ) 
if ( trouver_0 != multiple ) :
    print ( "[0 ; PI]" ) 
    x = trouver_0( cosinus, 0, pi )
else :
    print ( "[-5 ; 5[" ) 
    x = trouver_0( cosinus, -5, 5, pas )
print ( "x =", x )
print ( "f(x) =", cosinus(x) )
print()
  
if ( trouver_0 != multiple ) :  
    print ( "f(x) = tan(x)" ) 
    print ( "[-PI/2 ; PI/2]" ) 
    x = trouver_0( tan, -pi/2, pi/2 )
    print ( "x =", x )
    print ( "f(x) =", tangente(x) )
else :
    print ( "Pas d'étude de la tangente car la fonction est discontinue" )
print()
    
print ( "f(x) = -2x + 5" )
if ( trouver_0 != multiple ) : 
    print ( "[2 ; 3]" ) 
    x = trouver_0( lineaire, 2, 3 )
else :
    print ( "[-5 ; 5[" ) 
    x = trouver_0( lineaire, -5, 5, pas )
print ( "x =", x )
print ( "f(x) =", lineaire(x) )
print()
    
print ( "f(x) = -3*x^2 + 5x -1" ) 
if ( trouver_0 != multiple ) :
    print ( "[1 ; 2]" ) 
    x = trouver_0( quadratique, 1, 2 )
else :
    print ( "[-5 ; 5[" ) 
    x = trouver_0( quadratique, -5, 5, pas )
print ( "x =", x )
print ( "f(x) =", quadratique(x) )
print()
    
print ( "f(x) = x^3 + 2x^2 - 6x + 3 " ) 
if ( trouver_0 != multiple ) :
    print ( "[-5 ; -3]" ) 
    x = trouver_0( cubique, -5, -3 )
else :
    print ( "[-5 ; 5[" ) 
    x = trouver_0( cubique, -5, 5, pas )
print ( "x =", x )
print ( "f(x) =", cubique(x) )
print()