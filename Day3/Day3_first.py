file = open("input.txt","r")
inputs = file.read().split()
file.close()

def count(inputs,len_):
    zero = [0]*len_
    one = [0]*len_
    
    for b in range(len(inputs)):
        for number in range(len_):
            if inputs[b][number] == '0':
                zero[(len_*b+number)%len_] += 1
            elif inputs[b][number] == '1':
                one[(len_*b+number)%len_] += 1
    #A tuple with the number of zeros/ones in each position
    return (zero,one)

def gamma_mult_epsilon(zero_one,len_):
    gamma = ""
    epsilon = ""
    for number in range(len_):
        #Number of zeros > number of ones
        if zero_one[0][number] > zero_one[1][number]:
            gamma += "0"
            epsilon += "1"
        #Number of ones > number of zeros
        elif zero_one[1][number] > zero_one[0][number]:
            gamma += "1"
            epsilon += "0"
        else:
            gamma += "1"
            epsilon += "0"
            
    return int(gamma,2)*int(epsilon,2)

len_ = len(inputs[0])
def result(inputs,len_):
    print(gamma_mult_epsilon(count(inputs,len_),len_))   
