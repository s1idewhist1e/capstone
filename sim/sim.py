#!usr/bin/env python3

import sys, getopt, time

errors = []

# constants
class constants:
    NOP = 0x0
    STA = 0x1
    STB = 0x2
    LDA = 0x3
    LDB = 0x4
    SHL = 0x5
    SHR = 0x6
    AND = 0x7
    INV = 0x8
    INC = 0x9
    LIA = 0xA
    LIB = 0xB
    BNE = 0xC
    JMP = 0xD
    OUT = 0xE

def main(argv):
    inputFile = argv[0]
    instructions = parse(open(inputFile).read())

    execute(instructions)

def parse(file):

    labels = {};
    ops = [];
    lines = file.splitlines()

    lines = [a.split(";", 2)[0] for a in lines]

    opsIndex = 0;

    for i, line in enumerate(lines):
        if not line.isspace() and line:
            if not line[0].isspace():
                line = line.strip()
                if line[-1] != ":":
                    errors.append("Invalid label at line " + i)
                else:
                    labels[line[:-1]] = opsIndex
            else:
                line = line.strip()
                tokens = line.split()
                match tokens[0]:
                    case "NOP":
                        if len(tokens) != 1:
                            errors.append("Invalid number of tokens at line" + i)
                        ops.append((constants.NOP, None))
                    case "STA":
                        if len(tokens) != 2:
                            errors.append("Invalid number of tokens at line" + i)
                        ops.append((constants.STA, int(tokens[1], 16)))
                    case "STB":
                        if len(tokens) != 2:
                            errors.append("Invalid number of tokens at line" + i)
                        ops.append((constants.STB, int(tokens[1], 16)))
                    case "LDA":
                        if len(tokens) != 2:
                            errors.append("Invalid number of tokens at line" + i)
                        ops.append((constants.LDA, int(tokens[1], 16)))
                    case "LDB":
                        if len(tokens) != 2:
                            errors.append("Invalid number of tokens at line" + i)
                        ops.append((constants.LDB, int(tokens[1], 16)))
                    case "SHL":
                        if len(tokens) != 1:
                            errors.append("Invalid number of tokens at line" + i)
                        ops.append((constants.SHL, None))
                    case "SHR":
                        if len(tokens) != 1:
                            errors.append("Invalid number of tokens at line" + i)
                        ops.append((constants.SHR, None))
                    case "AND":
                        if len(tokens) != 1:
                            errors.append("Invalid number of tokens at line" + i)
                        ops.append((constants.AND, None))
                    case "INV":
                        if len(tokens) != 1:
                            errors.append("Invalid number of tokens at line" + i)
                        ops.append((constants.INV, None))
                    case "INC":
                        if len(tokens) != 1:
                            errors.append("Invalid number of tokens at line" + i)
                        ops.append((constants.INC, None))
                    case "LIA":
                        if len(tokens) != 2:
                            errors.append("Invalid number of tokens at line" + i)
                        ops.append((constants.LIA, int(tokens[1], 16)))
                    case "LIB":
                        if len(tokens) != 2:
                            errors.append("Invalid number of tokens at line" + i)
                        ops.append((constants.LIB, int(tokens[1], 16)))
                    case "BNE":
                        if len(tokens) != 1:
                            errors.append("Invalid number of tokens at line" + i)
                        ops.append((constants.BNE, None))
                    case "JMP":
                        if len(tokens) != 2:
                            errors.append("Invalid number of tokens at line" + i)                        
                        ops.append((constants.JMP, labels[tokens[1]]))
                    case "OUT":
                        if len(tokens) != 1:
                            errors.append("Invalid number of tokens at line" + i)
                        ops.append((constants.OUT, None))
                    case other:
                        errors.append("Invalid operation at line " + i)
                opsIndex += 1
    return ops
    
def execute(instructions):

    mem = [0x00] * 16
    areg = 0x00
    breg = 0x00

    pc = 0x00
    
    while pc < len(instructions):

        time.sleep(0.1)

        instr  = instructions[pc]

        areg &= 0xFF
        breg &= 0xFF
        pc &= 0xFF

        match instr[0]:
            case constants.NOP:
                print("NOP")
            case constants.STA:
                mem[int(instr[1])] = areg
            case constants.STB:
                mem[int(instr[1])] = breg
            case constants.LDA:
                areg = mem[int(instr[1])]
            case constants.LDB:
                breg = mem[int(instr[1])]

            case constants.SHL:
                areg = areg << (instr[1] & 0b111)
            case constants.SHR:
                areg = areg >> (instr[1] & 0b111)
            case constants.AND:
                areg = areg & breg
            case constants.INV:
                areg = ~areg
            case constants.INC:
                areg = areg + 1

            case constants.LIA:
                areg = instr[1]
            case constants.LIB:
                breg = instr[1]

            case constants.BNE:
                if (areg & 0xFF == breg & 0xFF):
                    pc += 1
            case constants.JMP:
                pc = instr[1] & 0xF
                pc -= 1

            case constants.OUT:
                for i in range(8):
                    if areg & (0b1 << 7 - i):
                        print("*", end = "")
                    else:
                        print("o", end = "")
                print()

            case other:
                raise Exception("Unknown operation!")

        pc += 1
            

if __name__ == "__main__":
    main(sys.argv[1:])
