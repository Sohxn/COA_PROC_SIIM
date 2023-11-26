from ALU import ALU
from datatransfer import datatransfer


class decoder:
    def __init__(self, instruction, data, register):
        # considering instruction string
        i = []  # 141343
        i.append(instruction[0])  # alu/data_transfer
        i.append(instruction[1:5])  # opcode
        i.append(instruction[5])  # op2 type
        i.append(instruction[6:9])  # op1 (destination)
        i.append(instruction[9:13])  # op2
        i.append(instruction[13:])  # op3
        if i[0] == "0":  # to be sent to ALU
            ALU(i, register)  # instruction is sent to ALU
        elif i[0] == "1":  # to be sent to ALU
            datatransfer(i, data, register)  # instruction is sent to datatransfer
        else:
            print("The instruction type is invalid")
