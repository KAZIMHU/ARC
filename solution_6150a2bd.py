'''
Function to solve ARC task
---------------------------
Task Number : 6150a2bd
'''

import sys
import numpy as np
from tools import loadJSON, plot


with open(sys.argv[1], 'r') as file:
    input_train,output_train,input_test,output_test = loadJSON(file) 

def solve(inputs):
    '''
    Used flip function from numpy package to reverse the order of elements in an array, 
    the elements are reordered but the shape is preserved.
    '''

    inp_array = np.array(inputs)
    test_result = np.flip(inp_array)
    return test_result

for inputs in (input_train + input_test):
    outputs = solve(inputs)
    #print(outputs)
    #print()

plt_list = [inputs, outputs]
plot(plt_list)