'''
27-Nov-2021
Common code for three tasks
'''
import json
import matplotlib.pyplot as plt


def loadJSON(file):

    '''
    This function reads the json file and splits the data into input train, output train, input test, output test. 
    '''    

    data = json.load(file)
    
    input_train = [data['train'][i]['input'] for i in range(len(data['train']))]
    output_train = [data['train'][i]['output'] for i in range(len(data['train']))]
    input_test = [data['test'][i]['input'] for i in range(len(data['test']))]
    output_test = [data['test'][i]['output'] for i in range(len(data['test']))]
    return input_train,output_train,input_test,output_test


def plot(input):

    '''
    This function is used for plotting grids
    '''
    
    for i in range(len(input)):
        plt.matshow(input[i])
    plt.show()