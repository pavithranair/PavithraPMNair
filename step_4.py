import numpy as np
#imports numpy as np. NumPy contains a multi-dimensional array
#and matrix data structures.

import time
#time provides many ways of representing time in code,
#such as objects, numbers, and strings.

with open('subset_elemets.txt') as f:
    subset_elements = f.read().split('\n')#stores all the elements in 'subset_elements.txt'
    
with open('all_elements.txt') as f:
    all_elements = f.read().split('\n')#stores all the elements in 'all_elements.txt'
    
def np_intersection(x, y):
    """Returns the intersection of the arrays passed as parameters using numpy module

    Parameters:
    x (array): An array
    y (array): An array

    Returns:
    array: intersection of x and y

    """
    return np.intersect1d(x, y)

def set_intersection(x, y):
    """Returns the intersection of the lists passed as parameters using set operations

    Parameters:
    x (list): A list
    y (list): A list 

    Returns:
    set: intersection of x and y

    """
    return set(x).intersection(y)

start = time.time()#stores the number of seconds passed since epoch
verified_elements = np_intersection(subset_elements, all_elements)#stores the intersection of subset_elements and all_elements
print(len(verified_elements))#prints length of intersection of subset_elements and all_elements
print('Duration: {} seconds'.format(time.time() - start))#prints time passed since start

start = time.time()#stores the number of seconds passed since epoch
verified_elements = set_intersection(subset_elements, all_elements)#stores the intersection of subset_elements and all_elements
print(len(verified_elements))#prints length of intersection of subset_elements and all_elements
print('Duration: {} seconds'.format(time.time() - start))#prints time passed since start

