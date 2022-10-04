# %% Ejercicio 2

def suma_matrix_buggy(A:list,B:list)->list:
    '''
    Realiza la suma de dos matrices de 2x2
    Parameters
    ----------
    A : (list) matriz de 2x2.
    B : (list) matriz de 2x2.
    Returns
    -------
    C : (list) = A+B.
    '''
    C=[[0,0],[0,0]]           
    for k in range(len(A)):
        C[k] = [A[k][i] + B[k][i] for i in range(len(B))]
    return C

    # C=[]               
    # for k in range(len(A)):
    #     C.append([A[k][i] + B[k][i] for i in range(len(A[0]))])
    # return C

def test_suma_matrix_buggy_ok():
    if suma_matrix_buggy([[1,2],[3,4]],[[3,4],[4,3]]) != [[4,6],[7,7]]:
        print('Error')
    else: print('OK')

def test_suma_matrix_buggy_zero():
    if suma_matrix_buggy([[1,1],[1,1]],[[-1,-1],[-1,-1]]) != [[0,0],[0,0]]:
        print('Error')
    else: print('OK')

def test_suma_matrix_buggy_neg():
    if suma_matrix_buggy([[-2,-2],[-2,-2]],[[-1,-1],[-1,-1]]) != [[-3,-3],[-3,-3]]:
        print('Error')
    else: print('OK')

if __name__ == '__main__':
    test_suma_matrix_buggy_ok()
    test_suma_matrix_buggy_zero()
    test_suma_matrix_buggy_neg()
