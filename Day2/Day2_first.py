file = open("input.txt","r")
inputs = file.read().split()
# print(inputs)
file.close()



def final_position(inputs):
    hor = 0
    depth = 0    
    
    for i in range(0,len(inputs)-1,2):
        if inputs[i] == "forward":
            hor += int(inputs[i+1])
        elif inputs[i] == "down":
            depth += int(inputs[i+1])
        elif inputs[i] == "up":
            depth -= int(inputs[i+1])
        else:
            print(f"Error with the inputs")    
    return hor * depth

print(final_position(inputs))

