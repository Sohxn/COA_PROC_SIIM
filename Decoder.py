import ALU

class decoder:
    def __init__(self,instruction):
        #considering instruction string
        i = [] #141343
        i.append(instruction[0]) #alu/data_transfer
        i.append(instruction[1:5]) #opcode
        i.append(instruction[5]) #1 bit code 
        i.append(instruction[6:9]) #op1 (destination)
        i.append(instruction[9:13]) #op2
        i.append(instruction[13:]) #op3
        
        if i[0] == '0':
            obj=ALU.ALU(i)
        else:
            #send i to data_transfer
            
        
        
    

            
        
        
        
