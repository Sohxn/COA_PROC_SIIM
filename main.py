import MemoryControl
import Decoder
class Main:
    main_memory = [[],[]]
    registers = (0,0,0,0,0,0,0,0)
    PC = 0
    instr_cnt=0;
    f = open("instructions.txt","r")
    instruction=f.readlines()
    obj1=MemoryControl.MemoryControl(instruction,main_memory)
    ##list of instructions is sent to MemoryControl which \
        # saves the instructions to main memory
    ##list of instructions stored in main_memory[0]

    for i in range (len(instruction)):
        obj2 = Decoder.decoder(main_memory[0][PC])
        PC+=1
    ##loop runs for every instruction
    ##each instruction is sent to decoder