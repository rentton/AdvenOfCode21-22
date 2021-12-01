file = open("input.txt","r")
inputs = file.read().split()
file.close()
for i in range(len(inputs)):
    inputs[i] = int(inputs[i])

def count_increased(inputs):
    n = 0
    for i in range(1,len(inputs)):
        if inputs[i] > inputs[i-1]:
            n+=1
    return n

print(count_increased(inputs))

