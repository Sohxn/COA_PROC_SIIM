class datatransfer:
    def __init__(self, a, data, register):
        index = int(a[3], 2)  # converting to decimal

        match a[1]:
            case "0101":  # LOAD
                if data[a[4]][0] == "1":  # if negative, taking 2's compliment
                    x = 1111111111111111 - int(data[a[4]])  # 1's complement
                    y = f"{x:016d}"
                    num = int(y[i], 2)  # converting to decimal
                    num = -1 - num  # 2's complement
                else:
                    num = int(data[a[4]], 2)  # converting to decimal
                register[index] = num  # loading from memory to regiter

            case "0110":  # STORE
                num = int(register[index])
                compl = bin(num)
                if num < 0:
                    compl = compl.replace("-0b", "")  # converting to 2's complement
                    compl = 1111111111111111 - int(compl)
                    compl = bin(int(str(compl), 2) + 1)[2:]
                else:
                    compl = f"{int(compl[2:]):016d}"
                data[a[4]] = compl  # storing from register to memory
                f = open("data.txt", "w")
                for i in data:
                    f.write(i + " " + data[i] + "\n")
                f.close()
            case _:
                print("Invalid operation")
