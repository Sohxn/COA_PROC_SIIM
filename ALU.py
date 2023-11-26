class ALU:
    def __init__(self, a, register):
        # OPERAND 1:

        op1 = int(a[3], 2)  # converting to decimal

        # OPERAND 2:

        if a[2] == "0":  # type of OPERAND 2 is register
            index = int(a[4], 2)  # converting to decimal
            self.op2 = register[index]  # accessing from list of registers

        else:  # OPERAND 2 is immediate value(in 2's complement)
            if a[4][0] == "1":  # if negative, taking 2's compliment
                x = 1111 - int(a[4])
                binary = f"{x:04d}"  # 1's complement
                self.op2 = int(binary, 2)  # converting to decimal
                self.op2 = -1 - self.op2  # 2's complement
            else:
                self.op2 = int(a[4], 2)  # converting to decimal

        # OPERAND 3

        index = int(a[5], 2)  # converting to decimal
        self.op3 = register[index]  # accessing from list of registers

        match a[1]:
            case "0000":  # ADD
                register[op1] = self.op2 + self.op3
            case "0001":  # SUBTRACT
                register[op1] = self.op2 - self.op3
            case "0010":  # AND
                register[op1] = self.op2 & self.op3
            case "0011":  # OR
                register[op1] = self.op2 | self.op3
            case "0100":  # XOR
                register[op1] = self.op2 ^ self.op3
            case _:
                print("Invalid operation")
