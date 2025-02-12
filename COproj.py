import re
import sys

def readfile(filename):
    labeldict = {}
    instructions = []
    with open(filename, "r") as file:
        lines = file.readlines()
    lineno = 0
    for line in lines:
        line = line.strip()
        if not line:
            continue
        if ":" in line:
            label, instruction = line.split(":", 1)
            labeldict[label.strip()] = lineno
            if instruction.strip():
                instructions.append(instruction.strip().split()) 
                lineno += 1
        else:
            instructions.append(line.split())
            lineno += 1

    return labeldict, instructions

def registers(register):
    registermap = {
        'zero': '00000', 'ra': '00001', 'sp': '00010', 'gp': '00011', 'tp': '00100',
        't0': '00101', 't1': '00110', 't2': '00111', 't3': '11100', 't4': '11101', 't5': '11110', 't6': '11111',
        's0': '01000', 'fp': '01000', 's1': '01001',
        'a0': '01010', 'a1': '01011', 'a2': '01100', 'a3': '01101', 'a4': '01110', 'a5': '01111', 'a6': '10000', 'a7': '10001', 
        's2': '10010', 's3': '10011', 's4': '10100', 's5': '10101','s6': '10110', 's7': '10111', 's8': '11000', 's9': '11001', 's10': '11010', 's11': '11011',
    }
    return registermap.get(register, None)

def binary_convertor(value, bits):
    value = int(value)
    if not (-2**(bits-1) <= value < 2**(bits-1)):
        print("out of range")
        exit()
    if value < 0:
        value = (1 << bits) + value
    binaryrep = bin(value)[2:]
    return '0' * (bits - len(binaryrep)) + binaryrep 

def r_type(data):
    opcode = '0110011'
    funct7_map = {'add': '0000000', 'sub': '0100000', 'sll': '0000000', 'slt': '0000000',
                  'xor': '0000000', 'srl': '0000000', 'or': '0000000', 'and': '0000000'}
    funct3_map = {'add': '000', 'sub': '000', 'sll': '001', 'slt': '010', 'xor': '100',
                  'srl': '101', 'or': '110', 'and': '111'}

    rd, rs1, rs2 = reg_add(data[1]), reg_add(data[2]), reg_add(data[3])
    if None in [rd, rs1, rs2]:
        print("Error: Invalid register in instruction.")
        return None
    
    return funct7_map[data[0]] + rs2 + rs1 + funct3_map[data[0]] + rd + opcode

def i_type(data):
    opcode_map = {
        'lw': ('0000011', '010'),
        'addi': ('0010011', '000'),
        'jalr': ('1100111', '000')
    }
    opcode, funct3 = opcode_map.get(data[0], (None, None))
    if not opcode:
        print("error: invalid I-type instruction")
        exit()
    imm = Binary_convertor(data[3], 12)
    return [imm, reg_add(data[2]), funct3, reg_add(data[1]), opcode]

#kmjninijk