file = open("input.txt","r")
inputs = file.read().split()
file.close()
for i in range(len(inputs)):
    inputs[i] = int(inputs[i])
    
def count_three_increased(input):
    n = 0
    for i in range(1,len(input)-2):
        a = input[i] + input[i+1] + input[i+2]
        b = input[i-1] + input[i] + input[i+1]
        if a > b:
            n+=1
    return n

print(count_three_increased(inputs))