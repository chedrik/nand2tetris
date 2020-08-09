import sys

from enum import Enum

sym_table = {'SP': 0,
             'LCL': 1,
             'ARG': 2,
             'THIS': 3,
             'THAT': 4,
             'R0': 0,
             'R1': 1,
             'R2': 2,
             'R3': 3,
             'R4': 4,
             'R5': 5,
             'R6': 6,
             'R7': 7,
             'R8': 8,
             'R9': 9,
             'R10': 10,
             'R11': 11,
             'R12': 12,
             'R13': 13,
             'R14': 14,
             'R15': 15,
             'SCREEN': 16384,
             'KBD': 24756,
             '__next_avail_addr': 16}  # Assumes no variable will be named this

jmp_def = {'0': '000',
           'JGT': '001',
           'JEQ': '010',
           'JGE': '011',
           'JLT': '100',
           'JNE': '101',
           'JLE': '110',
           'JMP': '111'}

dest_def = {'0': '000',
            'M': '001',
            'D': '010',
            'MD': '011',
            'A': '100',
            'AM': '101',
            'AD': '110',
            'AMD': '111'}

c_def = {'0': '0101010',
         '1': '0111111',
         '-1': '0111010',
         'D': '0001100',
         'A': '0110000',
         'M': '1110000',
         '!D': '0001101',
         '!A': '0110001',
         '!M': '1110001',
         '-D': '0001111',
         '-A': '0110011',
         '-M': '1110011',
         'D+1': '0011111',
         'A+1': '0110111',
         'M+1': '1110111',
         'D-1': '0001110',
         'A-1': '0110010',
         'M-1': '1110010',
         'D+A': '0000010',
         'D+M': '1000010',
         'D-A': '0010011',
         'D-M': '1010011',
         'A-D': '0000111',
         'M-D': '1000111',
         'D&A': '0000000',
         'D&M': '1000000',
         'D|A': '0010101',
         'D|M': '1010101'}


class Cmd(Enum):
    L = 0
    A = 1
    C = 2


def read_file(file_path):
    """ Reads a plaintext file and returns the list of lines"""
    try:
        with open(file_path) as file:
            lines = file.readlines()
    except FileNotFoundError:
        print("Can't find the file! Returning empty list of lines")
        lines = []
    return lines


def save_file(file_path, lines):
    """ Saves the machine code to a new file, overwriting the file if it already exists"""
    with open(file_path, "w") as file:
        for line in lines:
            file.write(line + '\n')
    return


def handle_whitespace(line):
    """Removes comments, new line , and returns only machine code relevant data"""
    new_l = ''
    no_comment = line.split("//")[0]
    if no_comment:
        new_l = no_comment.strip('\n').strip(' ')
    return new_l


def determine_cmd_type(cmd):
    """ Determines the type of command, one of L(loop), A, or C"""
    if cmd[0] == '(':
        return Cmd.L
    elif cmd[0] == '@':
        return Cmd.A
    else:
        return Cmd.C


def parse_c_cmd(cmd):
    """ Parses an 'c' command, using the c lookup from the language spec"""
    if '=' in cmd:
        split = cmd.split('=')
        jmp_bits = jmp_def['0']
        dest_bits = dest_def[split[0].replace(' ', '')]
        c_bits = c_def[split[1].replace(' ', '')]
    elif ';' in cmd:
        split = cmd.split(';')
        jmp_bits = jmp_def[split[1].replace(' ', '')]
        dest_bits = dest_def['0']
        c_bits = c_def[split[0].replace(' ', '')]
    else:
        print('ERROR: = or ; not found in C command: {}'.format(cmd))
        return ''
    return '111' + c_bits + dest_bits + jmp_bits


def parse_a_cmd(cmd):
    """ Parses an 'a' command, using the symbol table to resolve any symbols when needed"""
    addr = cmd[1:]
    try:
        val = int(addr)
    except ValueError:
        if addr not in sym_table:
            sym_table[addr] = sym_table['__next_avail_addr']
            sym_table['__next_avail_addr'] += 1
        val = sym_table[addr]
    return dec2bin(val)


def dec2bin(number):
    """ Converts a decimal to binary address and pads to be 16 digits for A commands"""
    raw_bin = bin(number)[2:]  # First two char are 0b
    padding = (16 - len(raw_bin)) * '0'
    return padding + raw_bin


def assemble():
    """ Main function to translate hack assembly to machine code"""
    if len(sys.argv) == 1:
        raise IOError("Expected an argument for passing the file path!!!")
    file_path = sys.argv[1]
    lines = read_file(file_path)

    code_lines = []
    lc = 0
    for line in lines:  # first pass
        cmd = handle_whitespace(line)
        if not cmd:
            continue
        cmd_type = determine_cmd_type(cmd)
        if cmd_type != Cmd.L:
            lc += 1
            code_lines.append(cmd)
        else:
            sym = cmd[1:-1]  # Remove the () to extract symbol
            if sym not in sym_table:
                sym_table[sym] = lc

    bin_code = []
    for line in code_lines:  # second pass
        cmd_type = determine_cmd_type(line)
        if cmd_type == Cmd.A:
            bin_code.append(parse_a_cmd(line))
        elif cmd_type == Cmd.C:
            bin_code.append(parse_c_cmd(line))
        else:
            raise ValueError("No L Commands should be present!!!")

    new_file_path = file_path.split('.')[0] + '.hack'
    save_file(new_file_path, bin_code)


if __name__ == '__main__':
    assemble()
