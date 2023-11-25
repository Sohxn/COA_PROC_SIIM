main_memory = [[],[]]
registers = [5,0,3,0,0,0,4,2]

class decoder:
    def __init__(self, instruction):
        #considering instruction string
        i = [] #141343
        i.append(instruction[0])    #alu/data_transfer
        i.append(instruction[1:5])  #opcode
        i.append(instruction[5])    #op2 type 
        i.append(instruction[6:9])  #op1 (destination)
        i.append(instruction[9:13]) #op2
        i.append(instruction[13:])  #op3
        if i[0] == "0":
            obj = ALU(i)                  #instruction is sent to ALU
        else:
            obj = datatransfer(i)         #instruction is sent to datatransfer

class datatransfer:
    pass
           
class ALU:
    def __init__(self,a):
        if a[2] == '0':                   #register
            index =int((a[4])[3])*1+int((a[4])[2])*2+int((a[4])[1])*4+int((a[4])[0])*8
            self.op2=registers[index]
        else:                             #immediate value(in 2's complement)
            if a[4][0] == '1':              #if negative, taking 2's compliment
                x=(1111-int(a[4])+1)
                bin = f'{x:04d}'
                print(bin)
                self.op2=-(int(bin[3])*1+int(bin[2])*2+int(bin[1])*4+int(bin[0])*8)    #converting to decimal            
            else:
                self.op2 =int((a[4])[3])*1+int((a[4])[2])*2+int((a[4])[1])*4+int((a[4])[0])*8   #converting to decimal

        
        
        index =int((a[5])[2])*1+int((a[5])[1])*2+int((a[5])[0])*4
        self.op3=registers[index]
        
        index =int((a[3])[2])*1+int((a[3])[1])*2+int((a[3])[0])*4
        
        match a[1]:
            case '0000':
                registers[index]=self.op2+self.op3
            case '0001':
                registers[index]=self.op2-self.op3
            case '0010':
                registers[index]=self.op2&self.op3
            case '0011':
                registers[index]=self.op2|self.op3
            case '0100':
                registers[index]=self.op2^self.op3
                            
        print(registers[index])    
        
        
class MemoryControl:
    def __init__(self,a,b):
        b[0]=a
        
        
class Main:
    PC = 0
    instr_cnt = 0
    f = open("COA_Project\instructions.txt","r")
    instruction=f.readlines()
    obj1 = MemoryControl(instruction,main_memory)       #list of instructions is sent to MemoryControl which
#                                                                           saves the instructions to main memory

    for i in range (len(instruction)):                              #loop runs for every instruction
        obj2 = decoder(main_memory[0][PC])                  #each instruction is sent to decoder
        PC += 1