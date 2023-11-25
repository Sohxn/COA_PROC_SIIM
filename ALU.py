from Main import Main

class ALU:
    def __init__(self,a):
        if a[2] == '0':                   #register
            index =int((a[4])[3])*1+int((a[4])[2])*2+int((a[4])[1])*4+int((a[4])[0])*8
            self.op2=Main.registers[index]
        else:                             #immediate value(in 2's complement)
            if a[4][0] == '1':              #if negative, taking 2's compliment
                x=(1111-int(a[4])+1)
                bin = f'{x:04d}'
                self.op2=-(int(bin[3])*1+int(bin[2])*2+int(bin[1])*4+int(bin[0])*8)    #converting to decimal            
            else:
                self.op2 =int((a[4])[3])*1+int((a[4])[2])*2+int((a[4])[1])*4+int((a[4])[0])*8   #converting to decimal
        
        index =int((a[5])[2])*1+int((a[5])[1])*2+int((a[5])[0])*4
        self.op3=Main.registers[index]
        
        index =int((a[3])[2])*1+int((a[3])[1])*2+int((a[3])[0])*4
        
        match a[1]:
            case '0000':
                Main.registers[index]=self.op2+self.op3
            case '0001':
                Main.registers[index]=self.op2-self.op3
            case '0010':
                Main.registers[index]=self.op2&self.op3
            case '0011':
                Main.registers[index]=self.op2|self.op3
            case '0100':
                Main.registers[index]=self.op2^self.op3
                            
        print(Main.registers[index])
