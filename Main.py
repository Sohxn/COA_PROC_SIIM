from Decoder import decoder

main_memory = [[], {}]
registers = [0, 0, 0, 0, 0, 0, 0, 0]


class Main:
    PC = 0
    f = open("program.txt", "r")
    instruction = f.readlines()
    main_memory[0] = instruction  # instructions saved to main_memory[0]
    f.close()

    f = open("data.txt", "r")
    datalist = f.readlines()
    for str in datalist:
        main_memory[1].update({(str[0:4]): (str[5:21])})  # data saved to main_memory[1]
    f.close()

    for i in range(len(instruction)):  # loop runs for every instruction
        decoder(
            main_memory[0][PC], main_memory[1], registers
        )  # each instruction is sent to decoder
        PC += 1
    print("Data in register is as follows:\n")
    print("Register\t\tData")
    for i in range(8):
        print("R", i, "\t\t\t", registers[i])
    print("\n\nData in memory is as follows:\n")
    for i in main_memory[1]:
        print(i, " : ", main_memory[1][i])
