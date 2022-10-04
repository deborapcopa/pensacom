
#%% Ejercicio 1

def rev_list_buggy(L):
    """
    input: L, a list
    Modifies L such that its elements are in reverse order
    return: reversed L
    """
    for i in range(len(L)//2):
        j = len(L) - i -1               # j = len(L) - i 
        temp = L[i]                     # L[i] = temp
        L[i] = L[j]
        L[j] = temp                     # L[j] = L[i]
    return L

def test_rev_list_ok():
    if rev_list_buggy([1,2,3,4]) != [4,3,2,1]:
        print('Error')
    else: print('OK')

def test_rev_list_empty():
    if rev_list_buggy([]) != []:
        print('Error')
    else: print('OK')

def test_rev_list_multiple_types_list():
    if rev_list_buggy([1,'2',(3,4),True]) != [True,(3,4),'2',1]:
        print('Error')
    else: print('OK')

if __name__ == '__main__':
    test_rev_list_ok()
    test_rev_list_multiple_types_list()
    test_rev_list_empty()
