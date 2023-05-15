import numpy as np

def inversion_diagonale ( A ) :
    return A
    
def inversion_inferieure ( A ) :
    return A
    
def inversion_superieure ( A ) :
    return A
    
def inversion_gauss ( A ) :
    return A
    
### Choix de la fonction à tester ###
fonction = inversion_diagonale
#fonction = inversion_inferieure
#fonction = inversion_superieure
#fonction = inversion_gauss
    
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

### Les tests (ne pas modifier) ###
def test ( fonction, A ) :
    inv = fonction ( np.copy(A) )
    res = np.dot ( A, inv )
    eye = np.eye ( len(A) )
    print ( eye )
    erreur = 0
    for i in range ( len(A) ) :
        for j in range ( len (A) ) :
            erreur += abs ( eye[i][j]-res[i][j] )
    if ( erreur < 0.0001 ) :
        print ( "    =" )
    else :
        print ( "    !=" )
    print ( A )
    print ( "    *" )
    print ( inv )   
    print()  

def test_multiple ( fonction, liste_matrices ) :
    for i in range ( len ( liste_matrices ) ) :
        test ( fonction, liste_matrices[i] )

### Affichage ###
print()

if ( fonction == inversion_diagonale ) :
    print("***** Diagonale *****\n")
    test_multiple ( fonction, matrices_diag )

if ( fonction == inversion_inferieure ) :
    print("***** Triangulaire inférieure *****\n")
    test_multiple ( fonction, matrices_inf )

if ( fonction == inversion_superieure ) :
    print("***** Triangulaire supérieure *****\n")
    test_multiple ( fonction, matrices_sup )

if ( fonction == inversion_gauss ) :
    print("***** Pivot de Gauss *****\n")
    test_multiple ( fonction, matrices )

