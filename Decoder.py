#import class decoder into main.py
class decoder:
    def __init__(self):
        self.instruct_map = {'0000': self.addop, '0001': self.subop, '0010': self.andop, '0011': self.orop}
        
    def decode(self, opcode):
        if opcode in self.instruct_map:
            op = self.instruct_map[opcode]
        else:
            print("ERROR:INVALID_OPCODE")
    
    #(depending on ALU code logic)   
    def addop:
        #add signal to ALU 
    def subop:
        #sub signal to ALU
    def andop:
        #and signal to ALU
    def orop:
        #or signal to ALU
            
        
        
        