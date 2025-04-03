import sys
input_file = sys.argv[1]  
output_file = sys.argv[2]  
def Binary_convertor(a, b):
    
    if a < 0:
        a = (1 << b) + a
    return format(a, '0{}b'.format(b))


def Decimal_converter(binary):
    if binary[0] == '1':
        decimal = int(binary, 2)
        inverted_bits = ''.join('1' if bit == '0' else '0' for bit in binary)
        positive_value = int(inverted_bits, 2) + 1
        decimal = -positive_value
    else:
        decimal = int(binary, 2)
    return decimal

def binary_to_decimal(binary_str):
    decimal = 0
    power = len(binary_str) - 1
    for digit in binary_str:
        decimal += int(digit) * (2 ** power)
        power -= 1
    return decimal

def Binary_xor(bin1, bin2):
    
    length = max(len(bin1), len(bin2))
    bin1 = bin1.zfill(length)
    bin2 = bin2.zfill(length)

    # Perform bitwise XOR
    result = ''
    for i in range(length):
        if bin1[i] != bin2[i]:
            result += '1'
        else:
            result += '0'

    return result

def sign_extend(binary_num, num_bits):
    
    if binary_num[0] == '1':
       
        extended_num = '1' * (num_bits - len(binary_num)) + binary_num
    else:
        
        extended_num = '0' * (num_bits - len(binary_num)) + binary_num

    return extended_num

datamemory={'0x00010000':'0b00000000000000000000000000000000','0x00010004':'0b00000000000000000000000000000000',
            '0x00010008':'0b00000000000000000000000000000000','0x0001000C':'0b00000000000000000000000000000000',
            '0x00010010':'0b00000000000000000000000000000000','0x00010014':'0b00000000000000000000000000000000',
            '0x00010018':'0b00000000000000000000000000000000','0x0001001C':'0b00000000000000000000000000000000',
            '0x00010020':'0b00000000000000000000000000000000','0x00010024':'0b00000000000000000000000000000000',
            '0x00010028':'0b00000000000000000000000000000000','0x0001002C':'0b00000000000000000000000000000000',
            '0x00010030':'0b00000000000000000000000000000000','0x00010034':'0b00000000000000000000000000000000',
            '0x00010038':'0b00000000000000000000000000000000','0x0001003C':'0b00000000000000000000000000000000',
            '0x00010040':'0b00000000000000000000000000000000','0x00010044':'0b00000000000000000000000000000000',
            '0x00010048':'0b00000000000000000000000000000000','0x0001004C':'0b00000000000000000000000000000000',
            '0x00010050':'0b00000000000000000000000000000000','0x00010054':'0b00000000000000000000000000000000',
            '0x00010058':'0b00000000000000000000000000000000','0x0001005C':'0b00000000000000000000000000000000',
            '0x00010060':'0b00000000000000000000000000000000','0x00010064':'0b00000000000000000000000000000000',
            '0x00010068':'0b00000000000000000000000000000000','0x0001006C':'0b00000000000000000000000000000000',
            '0x00010070':'0b00000000000000000000000000000000','0x00010074':'0b00000000000000000000000000000000',
            '0x00010078':'0b00000000000000000000000000000000','0x0001007C':'0b00000000000000000000000000000000'}

register_dict = {'00000':'0b00000000000000000000000000000000',
                 '00001':'0b00000000000000000000000000000000',
                 '00010':'0b00000000000000000000000101111100',
                 '00011':'0b00000000000000000000000000000000',
                 '00100':'0b00000000000000000000000000000000',
                 '00101':'0b00000000000000000000000000000000',
                 '00110':'0b00000000000000000000000000000000',
                 '00111':'0b00000000000000000000000000000000',
                 '01000':'0b00000000000000000000000000000000',
                 '01001':'0b00000000000000000000000000000000',
                 '01010':'0b00000000000000000000000000000000',
                 '01011':'0b00000000000000000000000000000000',
                 '01100':'0b00000000000000000000000000000000',
                 '01101':'0b00000000000000000000000000000000',
                 '01110':'0b00000000000000000000000000000000',
                 '01111':'0b00000000000000000000000000000000',
                 '10000':'0b00000000000000000000000000000000',
                 '10001':'0b00000000000000000000000000000000',
                 '10010':'0b00000000000000000000000000000000',
                 '10011':'0b00000000000000000000000000000000',
                 '10100':'0b00000000000000000000000000000000',
                 '10101':'0b00000000000000000000000000000000',
                 '10110':'0b00000000000000000000000000000000',
                 '10111':'0b00000000000000000000000000000000',
                 '11000':'0b00000000000000000000000000000000',
                 '11001':'0b00000000000000000000000000000000',
                 '11010':'0b00000000000000000000000000000000',
                 '11011':'0b00000000000000000000000000000000',
                 '11100':'0b00000000000000000000000000000000',
                 '11101':'0b00000000000000000000000000000000',
                 '11110':'0b00000000000000000000000000000000',
                 '11111':'0b00000000000000000000000000000000'}
def instruction_add(a,b):
    temp1 = Decimal_converter(a) 
    temp2 = Decimal_converter(b) 
    ans = temp1 + temp2
    ans_str=Binary_convertor(ans,32)
    return ans_str  

def instruction_sub(a,b):
    temp1 = Decimal_converter(a)  
    temp2 = Decimal_converter(b)  
    ans = temp1 - temp2
    ans_str = Binary_convertor(ans,32)
    return ans_str

def instruction_slt(a,b):
    temp1 = Decimal_converter(a)  
    temp2 = Decimal_converter(b)  
    ans0=Binary_convertor(0,32)
    ans1=Binary_convertor(1,32)
    if(temp2>temp1):
        return ans1
    else:
        return ans0

def instruction_srl(a,b):

    temp_a = int (a,2)
    temp = b[-5:]
    num = binary_to_decimal(temp)
    ans = temp_a>>num
   
    return format(ans, '032b')

def instruction_or(a,b):
    temp1 = int(a,2)  
    temp2 = int(b,2)  
    ans = temp1|temp2
    final_ans =Binary_convertor(ans,32)
    return final_ans 

def instruction_and(a,b):
    temp1 = int(a,2) 
    temp2 = int(b,2)  
    ans = temp1&temp2
    final_ans =Binary_convertor(ans,32)
    return final_ans 


def r_type(data):
    global PC
    opcode = data[-7:]
    rd = data[20:25]
    funct3 = data[17:20]
    rs1 = data[12:17]
    rs2 = data[7:12]
    funct7 = data[0:7]

    if (funct3=='000' and funct7=='0000000'): 
        register_dict[rd] = "0b"+instruction_add(register_dict[rs1][2:],register_dict[rs2][2:])
    elif(funct3=='000' and funct7 == '0100000'): 
        register_dict[rd] = "0b" + instruction_sub(register_dict[rs1][2:],register_dict[rs2][2:])
    elif(funct3=='101'):
        register_dict[rd] ="0b" +instruction_srl(register_dict[rs1][2:],register_dict[rs2][2:])
    elif(funct3=='010'): 
        register_dict[rd] ="0b" +instruction_slt(register_dict[rs1][2:],register_dict[rs2][2:])
    elif(funct3=='110'): 
        register_dict[rd] ="0b"+instruction_or(register_dict[rs1][2:],register_dict[rs2][2:])
    elif(funct3=='111'): 
        register_dict[rd] ="0b"+instruction_and(register_dict[rs1][2:],register_dict[rs2][2:])
    PC = instruction_add(PC,Binary_convertor(4,32))

PC='0'*32
def i_type(data):
    global PC
    opcode = data[-7::]
    rd = data[-12:-7]
    funct3 = data[-15:-12]
    rs1 = data[-20:-15]
    imm = data[-32:-20]

    if funct3=='010':
        
        temp=instruction_add(register_dict[rs1][2:],sign_extend(imm,32))
    
        temp1=hex(int(temp,2))[2:].lstrip('0')
        temp1='0x' + temp1.zfill(10- 2)
        register_dict[rd]=datamemory[temp1]
        PC = instruction_add(PC,Binary_convertor(4,32))

    elif funct3 == '000' and opcode=='0010011':
        
        register_dict[rd]="0b"+instruction_add(register_dict[rs1][2:],sign_extend(imm,32))
        PC = instruction_add(PC,Binary_convertor(4,32))
    
    else: 
        register_dict[rd]="0b"+instruction_add(PC,Binary_convertor(4,32))
        register_dict['00000'] = "0b00000000000000000000000000000000" 
        PC=instruction_add(register_dict[rs1][2:],sign_extend(imm,32))
        PC=PC[:-1]+'0'


def s_type(data):
    global PC
    opcode = data[-7::]
    imm1 = data[-12:-7]
    funct3 = data[-15:-12]
    rs1 = data[-20:-15]
    rs2 = data[-25:-20]
    imm2 = data[-32:-25]
    imm =imm2+imm1
    temp=instruction_add(register_dict[rs1][2:],sign_extend(imm,32))
    temp1=hex(int(temp,2))[2:].lstrip('0')
    temp1='0x' + temp1.zfill(8)
    datamemory[temp1] = register_dict[rs2]
    PC = instruction_add(PC,Binary_convertor(4,32))
def b_type(data):
    global PC
    opcode = data[-7::]
    funct3 = data[17:20]
    rs1 = register_dict[data[12:17]]
    rs2 = register_dict[data[7:12]]
    imm = data[0] + data[24] + data[1:7] +data[20:24]+"0"
    imm_decimal = Decimal_converter(sign_extend(imm, 32))
    if (rs1 == "0b00000000000000000000000000000000") and (rs2 == "0b00000000000000000000000000000000" and imm_decimal == 0):
        return
    
    if imm_decimal == 0:
        PC = instruction_add(PC, Binary_convertor(4, 32))
        return

    temp_PC = Decimal_converter(PC)//4
    temp_imm = Decimal_converter(sign_extend(imm,32))//4
    ans_PC = (temp_imm+temp_PC) * 4
    if(funct3=='000'):
        if(rs1==rs2):
            if rs1 != '0b' + '0' * 5: 
                PC = Binary_convertor(ans_PC, 32)
            return
    elif(funct3=='001'):
        if(rs1!=rs2):
            PC = Binary_convertor(ans_PC,32)
            return
    PC = instruction_add(PC,Binary_convertor(4,32))

def j_type(data):
    global PC
    opcode = data[-7::]
    rd = data[-12:-7]
    temp_imm=data[0]+data[12:20]+data[11]+data[1:11]+"0"
    temp_PC = Decimal_converter(PC)//4
    temp_imm = Decimal_converter(sign_extend(temp_imm,32))//4
    register_dict[rd]="0b"+instruction_add(PC,Binary_convertor(4,32))  

    ans_PC = (temp_imm+temp_PC) * 4
    PC = Binary_convertor(ans_PC,32)
    PC=PC[:-1]+'0'

def default_case(data):
    global PC
    print("error: ",data[0],)
    PC = instruction_add(PC,Binary_convertor(4,32))
    return

def Switch_case(case_value,data):
    switch_dict = {
         '0110011': r_type,
         '0000011': i_type,
         '0010011': i_type,
         '1100111': i_type,
         '0100011': s_type,
         '1100011': b_type,
         '1101111': j_type,
    }
    switch_dict.get(case_value,default_case)(data)
with open(output_file, 'w') as f:
    f.write("")
with open(input_file,"+r") as input_file:
    lines = [line.rstrip('\n') for line in input_file.readlines()]
with open(output_file, 'a') as f:
    while(True):
        a=lines[Decimal_converter(PC)//4]
        Switch_case(a[-7::],a)  
        register_dict["00000"] = "0b"+"0"*32
        f.write("0b"+PC+" ")
        for key,value in register_dict.items():
            f.write(value + " ")
        f.write('\n')
        if a == "00000000000000000000000001100011":
            break
    for key, value in datamemory.items():
        if key >= '0x00010000' and key <= '0x0001007C':
            f.write(key + ":" + value + "\n")
