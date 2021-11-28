
'''
Function to solve ARC task
---------------------------
Task Number : ce22a75a
'''

import sys
import numpy as np
from tools import loadJSON, plot


with open(sys.argv[1], 'r') as file:
    input_train,output_train,input_test,output_test = loadJSON(file)

def solve(inputs):
    
    '''
    The function returns a numpy array by replacing all zeros around a pattern with the corresponding pattern value.
    '''

    test_result = np.array(inputs)
    res = np.where(test_result > 0)
    try:
        
        for i in list(zip(res[0], res[1])):     
            for x in range(-1, 2):
                for y in range(-1, 2):
                    if (x != 0 or y != 0):
                        test_result[i[0] - x][i[1] - y] = 1
                        test_result[i[0]][i[1]] = 1 
    except IndexError: 
        pass                     
    return test_result


for inputs in (input_train + input_test):
    outputs = solve(inputs)
    #print(outputs)
    #print()
    

plt_list = [inputs, outputs]
plot(plt_list)