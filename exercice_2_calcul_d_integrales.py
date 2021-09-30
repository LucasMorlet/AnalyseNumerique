from math import *
from random import *

### Variables globales ###
nb_elements = 100

### Méthode de tirage aléatoire entre deux nombres (à utiliser pour la méthode de Monte-Carlo) ###
def aleatoire ( mini, maxi ) :
    return mini + (maxi-mini)*random()

### Quatre fonctions de calcul de l'intégrale par approche géométrique (à compléter) ###
def rectangle_a_droite ( fonction, a, b, nb_rectangles ) :
    return 0

def rectangle_a_gauche ( fonction, a, b, nb_rectangles ) :
    return 0
    
def rectangle_au_milieu ( fonction, a, b, nb_rectangles ) :
    return 0

def trapeze ( f, a, b, n ) :
    pas = (b-a) / n
    x = a
    somme = (f(a) + f(b)) / 2
    for _ in range(n-1):
        x += pas
        somme += f(x)
    return somme / n
    
def monte_carlo ( fonction, a, b, nb_intervalles ) :
    return 0
    
### Les fonctions à tester (ne pas modifier !) ###

# Identité
def identite ( x ) :
    return x
    
# Linéaire
def lineaire ( x ) :
    return -2*x + 5

# Quadratique 
def quadratique ( x ) :
    return -3*x*x + 5*x - 1
    
# Cubique
def cubique ( x ) :
    return x*x*x + 2*x*x - 6*x + 3

### L'affichage (ne pas modifier !) ###
print()

# Identité
fonction = identite
a = 0
b = 2
print ( "f(x) = x" )
print ( "[0 ; 2]" )
print ( "Gauche :", rectangle_a_gauche( fonction, a, b, nb_elements ) )
print ( "Droite :", rectangle_a_droite ( fonction, a, b, nb_elements ) )
print ( "Milieu :", rectangle_au_milieu( fonction, a, b, nb_elements ) )
print ( "Trapèze :", trapeze ( fonction, a, b, nb_elements ) )
print ( "Monte-Carlo :", monte_carlo ( fonction, a, b, nb_elements ) )
print()

# Sinus
fonction = sin
a = 0
b = pi/2
print ( "f(x) = sin(x)" )
print ( "[0 ; PI/2]" )
print ( "Gauche :", rectangle_a_gauche( fonction, a, b, nb_elements ) )
print ( "Droite :", rectangle_a_droite ( fonction, a, b, nb_elements ) )
print ( "Milieu :", rectangle_au_milieu( fonction, a, b, nb_elements ) )
print ( "Trapèze :", trapeze ( fonction, a, b, nb_elements ) )
print ( "Monte-Carlo :", monte_carlo ( fonction, a, b, nb_elements ) )
print()

# Cosinus
fonction = cos
a = 0
b = pi/2
print ( "f(x) = cos(x)" )
print ( "[0 ; PI/2]" )
print ( "Gauche :", rectangle_a_gauche( fonction, a, b, nb_elements ) )
print ( "Droite :", rectangle_a_droite ( fonction, a, b, nb_elements ) )
print ( "Milieu :", rectangle_au_milieu( fonction, a, b, nb_elements ) )
print ( "Trapèze :", trapeze ( fonction, a, b, nb_elements ) )
print ( "Monte-Carlo :", monte_carlo ( fonction, a, b, nb_elements ) )
print()

# Tangente
fonction = tan
a = 0
b = pi/4
print ( "f(x) = tan(x)" )
print ( "[0 ; PI/4]" )
print ( "Gauche :", rectangle_a_gauche( fonction, a, b, nb_elements ) )
print ( "Droite :", rectangle_a_droite ( fonction, a, b, nb_elements ) )
print ( "Milieu :", rectangle_au_milieu( fonction, a, b, nb_elements ) )
print ( "Trapèze :", trapeze ( fonction, a, b, nb_elements ) )
print ( "Monte-Carlo :", monte_carlo ( fonction, a, b, nb_elements ) )
print()

# Linéaire
fonction = lineaire
a = 0
b = 2.5
print ( "f(x) = -2x + 5" )
print ( "[0 ; 2.5]" )
print ( "Gauche :", rectangle_a_gauche( fonction, a, b, nb_elements ) )
print ( "Droite :", rectangle_a_droite ( fonction, a, b, nb_elements ) )
print ( "Milieu :", rectangle_au_milieu( fonction, a, b, nb_elements ) )
print ( "Trapèze :", trapeze ( fonction, a, b, nb_elements ) )
print ( "Monte-Carlo :", monte_carlo ( fonction, a, b, nb_elements ) )
print()

# Quadratique
fonction = quadratique
a = 0.25
b = 1.25
print ( "f(x) = -3x^2 + 5x - 1" )
print ( "[0.25 ; 1.25]" )
print ( "Gauche :", rectangle_a_gauche( fonction, a, b, nb_elements ) )
print ( "Droite :", rectangle_a_droite ( fonction, a, b, nb_elements ) )
print ( "Milieu :", rectangle_au_milieu( fonction, a, b, nb_elements ) )
print ( "Trapèze :", trapeze ( fonction, a, b, nb_elements ) )
print ( "Monte-Carlo :", monte_carlo ( fonction, a, b, nb_elements ) )
print()

# Cubique
fonction = cubique
a = -3.5
b = 0.5
print ( "f(x) = x^3 + 2x^2 - 6x + 3" )
print ( "[-3.5 ; 0.5]" )
print ( "Gauche :", rectangle_a_gauche( fonction, a, b, nb_elements ) )
print ( "Droite :", rectangle_a_droite ( fonction, a, b, nb_elements ) )
print ( "Milieu :", rectangle_au_milieu( fonction, a, b, nb_elements ) )
print ( "Trapèze :", trapeze ( fonction, a, b, nb_elements ) )
print ( "Monte-Carlo :", monte_carlo ( fonction, a, b, nb_elements ) )
print()