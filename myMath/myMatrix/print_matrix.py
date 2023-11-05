"""
    print_matrix accepts a list of lists or a numpy matrix and print to console
"""
def print_matrix(mat):
    if(mat == None):
        return
    
    for r in range(len(mat)): # type: ignore
        print('| ', end='')
        for c in range(len(mat[0])): # type: ignore
            print(f'{mat[r][c]} ', end='')
        print('| ')
