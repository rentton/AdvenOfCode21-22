from Day3_first import *

file = open("input.txt","r")
inputs = file.read().split()
file.close()

#Similar to first part
def single_count(inputs,index,kind):
    zeros = 0
    ones = 0
    
    for i in range(len(inputs)):
        if inputs[i][index] == '0':
            zeros+=1
        elif inputs[i][index] == '1':
            ones+=1
    
    if kind == 'O2':
        return ones >= zeros
    elif kind == 'CO2':
        return zeros > ones
        

def rating(inputs, kind):
    #Hard copy
    ins = inputs.copy()
    it = 0
    while len(ins) > 1:
        mask = int(single_count(ins,it,kind))
        binary = 0
        while binary < len(ins):
            if ins[binary][it] != str(mask):
                ins.pop(binary)
            else:
                binary += 1
        it+=1
    return ins.pop()

def result(inputs):
    a = rating(inputs,'O2')
    b = rating(inputs,'CO2')

    return int(a,2)*int(b,2)


print(result(inputs))        
        
    