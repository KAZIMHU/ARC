
'''
Function to solve ARC task
---------------------------
Task Number : 1cf80156
'''

import sys
import numpy as np
from tools import loadJSON, plot


with open(sys.argv[1], 'r') as file:
    input_train,output_train,input_test,output_test = loadJSON(file)


def solve(inputs):
    '''
    This function slices the minimum and maximum value of rows and columns for the given input and returns a numpy array.
    '''

    inp_array = np.array(inputs)
    res = np.where(inp_array > 0)
    col_min = min(res[1])
    col_max = max(res[1])
    row_min = min(res[0])
    row_max = max(res[0])
    test_result = []
    for i in range(row_min,row_max + 1):
        for j in range(col_min,col_max + 1):
            test_result.append(inp_array[i][j])
    test_result = np.reshape(test_result,(row_max-row_min + 1,col_max-col_min + 1))
    return test_result


for inputs in (input_train + input_test):
    outputs = solve(inputs)
    #print(outputs)
    #print() 
    
plt_list = [inputs, outputs]
plot(plt_list)