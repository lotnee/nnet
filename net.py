import numpy as np
import scipy.special
import random
from defs import *

class Net():
    def __init__(self,num_input,num_hidden,num_output):
        self.num_input = num_input
        self.num_hidden = num_hidden
        self.num_output = num_output
        self.weight_input_hidden = np.random.normal(0.0,0.5,size = (self.num_hidden,self.num_input))
        self.weight_hidden_output = np.random.normal(0.0,0.5,size = (self.num_output,self.num_hidden))
        self.activation_function = lambda x: scipy.special.expit(x)

    def get_outputs(self,inputs_list):
        inputs = np.array(inputs_list,ndmin = 2).T
        hidden_inputs = np.dot(self.weight_input_hidden,inputs)
        hidden_outputs = self.activation_function(hidden_inputs)
        final_inputs = np.dot(self.weight_hidden_output,hidden_outputs)
        final_outputs = self.activation_function(final_inputs)
        return final_outputs
    
    def get_max_value(self,inputs_list):
        outputs = self.get_outputs(inputs_list)
        return np.max(outputs)
    def modify_weights(self):
        Net.modify_array(self.weight_input_hidden)
        Net.modify_array(self.weight_hidden_output)
    def create_mixed_weights(self,net1,net2):
        self.weight_input_hidden = Net.get_mix_from_arrays(net1.weight_input_hidden, net2.weight_input_hidden)
        self.weight_hidden_output = Net.get_mix_from_arrays(net1.weight_hidden_output,  net2.weight_hidden_output)

    def modify_array(a):
        for x in np.nditer(a,op_flags=['readwrite']):
            if random.random() < MUTATION_WEIGHT_MODIFY_CHANCE:
                x[...] = np.random.random_sample() - 0.5

    def get_mix_from_arrays(arr1,arr2):
        total_entries = arr1.size
        num_rows = arr1.shape[0]
        num_cols = arr1.shape[1]
        num_to_take = total_entries - int(total_entries * MUTATION_ARRAY_MIX_PERC)
        idx = np.random.choice(np.arange(total_entries),num_to_take,replace=False)
        res = np.random.rand(num_rows,num_cols)
        for row in range(0,num_rows):
            for col in range(0, num_cols):
                index = row * num_cols + col 
                if index in idx:
                    res[row][col] =arr1[row][col]
                else:
                    res[row][col] = arr2[row][col]
        return res

        