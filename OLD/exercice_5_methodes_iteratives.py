import numpy as np

def inversion_diagonale ( A ) :
    return A
    
def inversion_inferieure ( A ) :
    return A
    
def resolution_iterative ( inv_M, N, b ) :
    return np.array([0.0]*len(A))

def resolution_jacobi ( A, b ) :
    return np.array([0.0]*len(A))
    
def resolution_gauss_siedel ( A, b ) :
    return np.array([0.0]*len(A))

    
### Choix de la fonction à tester ###
fonction = resolution_jacobi
#fonction = resolution_gauss_siedel

    
### Les matrices et images à tester (trois matrices 3x3) ###

matrices = []
matrices.append( np.array([[ 2.0, 1.0, 0.0 ], [ 1.0, 3.0, 1.0 ], [ 1.0, 1.0, 3.0 ]]) )
matrices.append( np.array([[ 0.6, -0.3, 0.1 ],[ -0.1, 0.4, 0.3 ], [ -0.2, 0.1, -0.5 ]]) )
matrices.append(np.array([ [ 5.0, 2.0, -1.0 ],[ 1.0, 6.0, -3.0 ], [ 2.0, 1.0, 4.0 ] ]))

images = []
images.append(np.array([ 4.2, 1.4, 2.3 ]))
images.append(np.array([ 0.4, -1.5, 1.6 ]))
images.append(np.array([ 0.7, -6.0, -5.7 ]))

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

if ( fonction == resolution_jacobi ) :
    print("***** Jacobi *****\n")
    test_multiple ( fonction, matrices, images )

if ( fonction == resolution_gauss_siedel ) :
    print("***** Gauss-Siedel *****\n")
    test_multiple ( fonction, matrices, images )


