import numpy as np


def calculate(lst):
    
    if(len(lst) < 9):
        raise ValueError("List must contain nine numbers.")
    
    matrix = np.reshape(lst, (3, 3))
    dict = {}
    mean = [
        [np.mean(matrix, axis=0)],   
        [np.mean(matrix, axis=1)],   
        np.mean(lst)                     
    ]
    dict['mean']= mean
    variance = [
        [np.var(matrix,axis=0)],
        [np.var(matrix,axis=1)],
        np.var(lst)
    ]
    dict['variance']= variance
    std_var = [
        [np.std(matrix,axis=0)],
        [np.std(matrix,axis=1)],
        np.std(lst)
    ]
    dict['std_var']= std_var
    max = [
        [np.max(matrix,axis=0)],
        [np.max(matrix,axis=1)],
        np.max(lst)
    ]
    dict['max']= max
    min = [
        [np.min(matrix,axis=0)],
        [np.min(matrix,axis=1)],
        np.min(lst)
    ]
    dict['min']= min
    sum = [
        [np.sum(matrix,axis=0)],
        [np.sum(matrix,axis=1)],
        np.sum(lst)
    ]
    dict['sum']= sum
    
    return dict

    