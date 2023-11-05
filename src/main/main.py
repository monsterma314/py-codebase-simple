import sys

print(sys.path)

from myMath.matematicas import * # imports all of the functions in matematicas.py

from myPrints.printing_ints import int_print # imports all of the functions in int_print.py

if __name__ == '__main__':
    a = 10
    b = 20
    c = ryan_mult(a, b)
    int_print(c) # should print 'int a = 200'