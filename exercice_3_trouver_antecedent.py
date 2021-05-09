import numpy as np

def resolution_diagonale ( A, b ) :
    return np.array([0.0]*len(A))
    
def resolution_inferieure ( A, b ) :
    return np.array([0.0]*len(A))
    
def resolution_superieure ( A, b ) :
    return np.array([0.0]*len(A)) 
    
def resolution_gauss ( A, b ) :
    return np.array([0.0]*len(A))
    
def resolution_LU ( A, b ) :
    return np.array([0.0]*len(A))
    
### Choix de la fonction à tester ###
fonction = resolution_diagonale
#fonction = resolution_inferieure
#fonction = resolution_superieure
#fonction = resolution_gauss
#fonction = resolution_LU
    
### Les matrices et images à tester (deux matrices 3x3 et une matrice 4x4) ###
matrices_diag = []
matrices_diag.append(np.array([[ 4.2, 0, 0 ],[0, 1.4, 0], [0, 0, 2.3]]))
matrices_diag.append(np.array([[ -1.6, 0, 0 ],[0, 8.1, 0], [0, 0, -3.1]]))
matrices_diag.append(np.array([[ -7.1, 0, 0, 0 ],[0, 6.8, 0, 0], [0, 0, -2.1, 0], [0, 0, 0, 9.1]]))

matrices_sup = []
matrices_sup.append(np.array([[ 4.2, 1.1, 7.3 ],[0, 1.4, 2.4], [ 0, 0, 2.3]]))
matrices_sup.append(np.array([[ 1.1, -6.7, 9.3 ],[0, -4.3, 0.2], [ 0, 0, -3.4]]))
matrices_sup.append(np.array([[ 5.7, 5.6, -5.3, 6.0 ],[ 0, -1.6, 4.7, 1.5], [0, 0, -7.3, 3.2], [0, 0, 0, 1.8]]))

matrices_inf = []
matrices_inf.append(np.array([[ 6.6, 0, 0 ],[ 0.1, 1.2, 0], [ 5.6, 5.9, 9.0 ]]))
matrices_inf.append(np.array([[ 7.7, 0, 0 ], [ 4.1, 3.3, 0 ], [ 3.1, 5.3, 6.9]]))
matrices_inf.append(np.array([[ -1.9, 0, 0, 0 ],[5.2, 8.9, 0, 0], [-7.9, 3.6, -9.8, 0], [8.4, -1.5, -7.6, 0.9]]))

matrices = []
matrices.append( np.array([[ 3.6, 2.1, 5.5 ],[1.7, 1.3, 2.4], [ 7.1, 6.8, 2.3]]) )
matrices.append( np.array([[ 2.2, 4.1, 1.9 ], [ -1.7, -3.0, 1.6 ], [ 4.5, -7.4, 2.1 ]]) )
matrices.append(np.array([[ -0.7, 6.0, -9.1, 4.2 ],[4.2, 2.8, -4.7, 3.9], [-2.5, 4.3, -9.3, 3.9], [-5.7, 2.0, 5.3, -9.9]]))

images = []
images.append(np.array([ 4.2, 1.4, 2.3 ]))
images.append(np.array([ 0.4, -1.5, 1.6 ]))
images.append(np.array([ 0.7, -6.0, -5.7, 1.6 ]))

### Les tests (ne pas modifier) ###
def test ( fonction, A, b ) :
    x = fonction ( np.copy(A), np.copy(b) )
    res = np.dot ( A, x )
    print ( b )
    erreur = 0
    for i in range ( len(b) ) :
        erreur += abs ( res[i]-b[i] )
    if ( erreur < 0.0001 ) :
        print ( "    =" )
    else :
        print ( "    !=" )
    print ( A )
    print ( "    *" )
    print ( x )   
    print()  

def test_multiple ( fonction, liste_matrices, listes_images ) :
    for i in range ( len ( liste_matrices ) ) :
        test ( fonction, liste_matrices[i], listes_images[i] )

### Affichage ###
print()

if ( fonction == resolution_diagonale ) :
    print("***** Diagonale *****\n")
    test_multiple ( fonction, matrices_diag, images )

if ( fonction == resolution_inferieure ) :
    print("***** Triangulaire inférieure *****\n")
    test_multiple ( fonction, matrices_inf, images )

if ( fonction == resolution_superieure ) :
    print("***** Triangulaire supérieure *****\n")
    test_multiple ( fonction, matrices_sup, images )

if ( fonction == resolution_gauss ) :
    print("***** Pivot de Gauss *****\n")
    test_multiple ( fonction, matrices, images )

if ( fonction == resolution_LU ) :
    print("***** Méthode LU *****\n")
    test_multiple ( fonction, matrices, images )

