import sys
import os

from enum import Enum


class Cmd(Enum):
    add = 0
    sub = 1
    neg = 2
    eq = 3
    gt = 4
    lt = 5
    aand = 6
    oor = 7
    nnot = 8
    pop = 9
    push = 10
    label = 11
    ifgt = 12
    goto = 13
    function = 14
    ret = 15
    call = 16


ptrs = {
    'local': 'LCL',
    'argument': 'ARG',
    'this': 'THIS',
    'that': 'THAT'
}

inc_sp = ("@SP // SP++\n"
          "M=M+1\n")
dec_sp = ("@SP // SP--\n"
          "M=M-1\n")
mem_addr = ("@{}\n"
            "D=A\n"
            "@{}\n"
            "D=D+M\n"
            "@R13\n"
            "M=D\n")  # pass the val first, then ptr name. Stores val in R13
set_sp_to_adr_ptr = ("@R13\n"
                     "A=M\n"
                     "D=M\n"
                     "@SP\n"
                     "A=M\n"
                     "M=D\n")
set_adr_ptr_to_sp = ("@SP\n"
                     "A=M\n"
                     "D=M\n"
                     "@R13\n"
                     "A=M\n"
                     "M=D\n")
set_sp_to_d = ("@SP  // *SP=D\n"
               "A=M\n"
               "M=D\n")


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
    """ Saves the assembly code to a new file, overwriting the file if it already exists"""
    with open(file_path, "w") as file:
        for line in lines:
            file.write(line + '\n')
    return


def handle_whitespace(line):
    """Removes comments, new line, and returns assembly relevant data"""
    new_l = ''
    no_comment = line.split("//")[0]
    if no_comment:
        new_l = no_comment.strip('\n').strip(' ')
    return new_l


def determine_cmd_type(cmd):
    """ Determines the type of command, see Cmd enum for options"""
    try:
        cmd_type = Cmd[cmd]
    except KeyError:
        if cmd == 'and':
            cmd_type = Cmd.aand
        elif cmd == 'or':
            cmd_type = Cmd.oor
        elif cmd == 'not':
            cmd_type = Cmd.nnot
        elif cmd == 'if-goto':
            cmd_type = Cmd.ifgt
        elif cmd == 'return':
            cmd_type = Cmd.ret
        else:
            raise ValueError('Unrecognized command {}!'.format(cmd))
    return cmd_type


def convert_to_asm(cmd_split, cmd_type, file_path):
    if cmd_type == Cmd.nnot:
        return _convert_pop(['push', 'math', 'R15'], '') + \
               ("@R15\n"
                "M=!M\n") + _convert_push(['push', 'math'], '')
    elif cmd_type == Cmd.oor:
        return _convert_pop(['push', 'math', 'R14'], '') + _convert_pop(['push', 'math', 'R15'], '') + \
               ("@R14\n"
                "D=M\n"
                "@R15\n"
                "M=D|M\n") + _convert_push(['push', 'math'], '')
    elif cmd_type == Cmd.aand:
        return _convert_pop(['push', 'math', 'R14'], '') + _convert_pop(['push', 'math', 'R15'], '') + \
               ("@R14\n"
                "D=M\n"
                "@R15\n"
                "M=D&M\n") + _convert_push(['push', 'math'], '')
    elif cmd_type == Cmd.add:
        return _convert_pop(['push', 'math', 'R14'], '') + _convert_pop(['push', 'math', 'R15'], '') + \
               ("@R14\n"
                "D=M\n"
                "@R15\n"
                "M=D+M\n") + _convert_push(['push', 'math'], '')
    elif cmd_type == Cmd.sub:
        return _convert_pop(['push', 'math', 'R14'], '') + _convert_pop(['push', 'math', 'R15'], '') + \
               ("@R14\n"
                "D=M\n"
                "@R15\n"
                "M=M-D\n") + _convert_push(['push', 'math'], '')
    elif cmd_type == Cmd.neg:
        return _convert_pop(['push', 'math', 'R15'], '') + \
               ("@R15\n"
                "M=-M\n") + _convert_push(['push', 'math'], '')
    elif cmd_type == Cmd.eq:
        convert_to_asm.counter += 1
        return _convert_pop(['push', 'math', 'R14'], '') + _convert_pop(['push', 'math', 'R15'], '') + \
               ("@R14\n"
                "D=M\n"
                "@R15\n"
                "D=M-D\n"
                "M=D \n"
                "@TRUE{0}\n"
                "D;JEQ\n"
                "@R15\n"
                "M=0\n"
                "(BACK{0})\n"
                ).format(convert_to_asm.counter) + _convert_push(['push', 'math'], '')
    elif cmd_type == Cmd.gt:
        convert_to_asm.counter += 1
        return _convert_pop(['push', 'math', 'R14'], '') + _convert_pop(['push', 'math', 'R15'], '') + \
               ("@R14\n"
                "D=M\n"
                "@R15\n"
                "D=M-D\n"
                "M=D \n"
                "@TRUE{0}\n"
                "D;JGT\n"
                "@R15\n"
                "M=0\n"
                "(BACK{0})\n"
                ).format(convert_to_asm.counter) + _convert_push(['push', 'math'], '')
    elif cmd_type == Cmd.lt:
        convert_to_asm.counter += 1
        return _convert_pop(['push', 'math', 'R14'], '') + _convert_pop(['push', 'math', 'R15'], '') + \
               ("@R14 \n"
                "D=M \n"
                "@R15 \n"
                "D=M-D \n"
                "M=D \n"
                "@TRUE{0} \n"
                "D;JLT \n"
                "@R15 \n"
                "M=0\n"
                "(BACK{0})\n"
                ).format(convert_to_asm.counter) + _convert_push(['push', 'math'], '')
    elif cmd_type == Cmd.pop:
        return _convert_pop(cmd_split, file_path)
    elif cmd_type == Cmd.push:
        return _convert_push(cmd_split, file_path)
    elif cmd_type == Cmd.label:
        return "({})\n".format(cmd_split[1])
    elif cmd_type == Cmd.ifgt:
        return dec_sp + ("@SP\n"
                         "A=M\n"
                         "D=M\n"
                         "@{}\n"
                         "D; JNE\n").format(cmd_split[1])  # + dec_sp + set_adr_ptr_to_sp
    elif cmd_type == Cmd.goto:
        return ("@{}\n"
                "0; JMP\n").format(cmd_split[1])
    elif cmd_type == Cmd.function:
        temp = "({})\n".format(cmd_split[1])
        for i in range(int(cmd_split[2])):
            temp += _convert_push(["push", "constant", "0"], None)
        return temp
    elif cmd_type == Cmd.ret:
        return ("@LCL // endframe=LCL \n"
                "D=M\n"
                "@FRAME\n"
                "M=D\n") + \
               ("@FRAME // set retaddr \n"
                "D=M\n"
                "@5\n"
                "D=D-A\n"
                "A=D\n"
                "D=M\n"
                "@RET\n"
                "M=D\n") + _convert_pop(["pop", "argument", "0"], None) + \
               ("@ARG // SP = ARG + 1\n"
                "D=M+1\n"
                "@SP\n"
                "M=D\n") + \
               ("@FRAME // set THAT \n"
                "D=M\n"
                "@1\n"
                "D=D-A\n"
                "A=D\n"
                "D=M\n"
                "@THAT\n"
                "M=D\n") + \
               ("@FRAME // set THIS \n"
                "D=M\n"
                "@2\n"
                "D=D-A\n"
                "A=D\n"
                "D=M\n"
                "@THIS\n"
                "M=D\n") + \
               ("@FRAME // set ARG \n"
                "D=M\n"
                "@3\n"
                "D=D-A\n"
                "A=D\n"
                "D=M\n"
                "@ARG\n"
                "M=D\n") + \
               ("@FRAME // set LCL \n"
                "D=M\n"
                "@4\n"
                "D=D-A\n"
                "A=D\n"
                "D=M\n"
                "@LCL\n"
                "M=D\n") + \
               ("@RET // goto ret \n"
                "A=M\n"
                "0; JMP\n")
    elif cmd_type == Cmd.call:
        convert_to_asm.fcn_counter += 1

        return ("@FCN_RETURN_{} // push return addr to label\n"
                "D=A\n"
                "@SP\n"
                "A=M\n"
                "M=D\n").format(convert_to_asm.fcn_counter) + inc_sp + _convert_push(["push", "call", "LCL"], None) + \
               _convert_push(["push", "call", "ARG"], None) + \
               _convert_push(["push", "call", "THIS"], None) + _convert_push(["push", "call", "THAT"], None) + \
               ("@SP // ARG = SP-5-nAargs\n"
                "D=M\n"
                "@{}\n"
                "D=D-A\n"
                "@ARG\n"
                "M=D\n").format(5 + int(cmd_split[2])) + \
               ("@SP // LCL = SP \n"
                "D=M\n"
                "@LCL\n"
                "M=D\n") + \
               ("@{} // go to fcn \n"
                "0; JMP\n").format(cmd_split[1]) + \
               "(FCN_RETURN_{})\n".format(convert_to_asm.fcn_counter)
    else:
        raise ValueError('Unrecognized command type {}!'.format(cmd_type))


def _convert_push(cmd_split, file_path):
    if cmd_split[1] == 'constant':
        asm_cmd = ("@{}  // D=Val\n"
                   "D=A\n").format(cmd_split[2]) + set_sp_to_d + inc_sp
    elif cmd_split[1] in ('local', 'this', 'that', 'argument'):
        asm_cmd = mem_addr.format(cmd_split[2], ptrs[cmd_split[1]]) + set_sp_to_adr_ptr + inc_sp
    elif cmd_split[1] == 'static':
        asm_cmd = "@{}.{}\n" \
                  "D=M\n".format(file_path.split('.')[0], cmd_split[2]) + set_sp_to_d + inc_sp
    elif cmd_split[1] == 'temp':
        asm_cmd = ("@{}\n"
                   "D=A\n"
                   "@{}\n"
                   "D=D+A\n"
                   "@R13\n"
                   "M=D\n").format(cmd_split[2], 5).format(cmd_split[2], 5) + set_sp_to_adr_ptr + inc_sp
    elif cmd_split[1] == 'pointer':
        if cmd_split[2] == "0":
            asm_cmd = ("@THIS\n"
                       "D=M\n") + set_sp_to_d + inc_sp
        elif cmd_split[2] == "1":
            asm_cmd = ("@THAT\n"
                       "D=M\n") + set_sp_to_d + inc_sp
        else:
            raise ValueError("Unrecognized ptr value for {}".format(cmd_split))
    elif cmd_split[1] == 'math':
        asm_cmd = ("@R15  // D=Val\n"
                   "D=M\n") + set_sp_to_d + inc_sp
    elif cmd_split[1] == 'call':
        asm_cmd = ("@{} // push {}\n"
                   "D=M\n"
                   "@SP\n"
                   "A=M\n"
                   "M=D\n"
                   "@SP\n"
                   "M=M+1\n").format(cmd_split[2], cmd_split[2])
    else:
        raise ValueError("Unrecognized push command {}".format(cmd_split))

    return asm_cmd


def _convert_pop(cmd_split, file_path):
    if cmd_split[1] == 'constant':
        raise ValueError("Constant cannot pop!")
    elif cmd_split[1] in ('local', 'this', 'that', 'argument'):
        asm_cmd = mem_addr.format(cmd_split[2], ptrs[cmd_split[1]]) + dec_sp + set_adr_ptr_to_sp
    elif cmd_split[1] == 'static':
        asm_cmd = dec_sp + ("@SP\n"
                            "A=M\n"
                            "D=M\n") + "@{}.{}\n" \
                                       "M=D\n".format(file_path.split('.')[0], cmd_split[2])
    elif cmd_split[1] == 'temp':
        asm_cmd = ("@{}\n"
                   "D=A\n"
                   "@{}\n"
                   "D=D+A\n"
                   "@R13\n"
                   "M=D\n").format(cmd_split[2], 5) + dec_sp + set_adr_ptr_to_sp
    elif cmd_split[1] == 'pointer':
        if cmd_split[2] == "0":
            asm_cmd = dec_sp + ("@SP\n"
                                "A=M\n"
                                "D=M\n"
                                "@THIS\n"
                                "M=D\n")
        elif cmd_split[2] == "1":
            asm_cmd = dec_sp + ("@SP\n"
                                "A=M\n"
                                "D=M\n"
                                "@THAT\n"
                                "M=D\n")
        else:
            raise ValueError("Unrecognized ptr value for {}".format(cmd_split))
    elif cmd_split[1] == 'math':
        asm_cmd = dec_sp + ("@SP\n"
                            "A=M\n"
                            "D=M\n"
                            "@{}\n"
                            "M=D\n").format(cmd_split[2])
    else:
        raise ValueError("Unrecognized pop command {}".format(cmd_split))

    return asm_cmd


def translate():
    """ Main function to translate vm code to hack assembly"""
    # if len(sys.argv) == 1:
    # raise IOError("Expected an argument for passing the file path!!!")

    # file_path = sys.argv[1]

    file_path = '/Users/chasensherman/Desktop/nand2tetris/projects/08/FunctionCalls/FibonacciElement'

    convert_to_asm.counter = 0
    convert_to_asm.fcn_counter = 0
    asm_lines = []


    if os.path.isdir(file_path):
        asm_lines.append(("@256  // Sys init\n"
                          "D=A\n"
                          "@SP\n"
                          "M=D\n"))
        asm_lines.append(convert_to_asm(["call", "Sys.init", "0"], Cmd.call, None))
        f = os.listdir(file_path)
        files = []
        for file in f:
            if '.vm' in file:
                files.append(os.path.join(file_path,file))
    else:
        files = [file_path]
    for file in files:
        lines = read_file(file)
        for line in lines:  # first pass
            cmd = handle_whitespace(line)
            if not cmd:
                continue
            cmd_split = cmd.split(' ')
            cmd_type = determine_cmd_type(cmd_split[0])
            asm = convert_to_asm(cmd_split, cmd_type, file.split('/')[-1][:-3])
            asm_lines.append('//' + cmd)
            asm_lines.append(asm)
    asm_lines.append(("(END)  // infinite end-of-program loop\n"
                      "\t@END\n"
                      "\t0; JMP\n"))
    i = 1
    while i <= convert_to_asm.counter:
        asm_lines.append(("(TRUE{0}) \n"
                          "\t@R15 \n"
                          "\tM=-1 \n"
                          "\t@BACK{0}\n"
                          "\t0;JMP\n"
                          ).format(i))
        i += 1
    if os.path.isdir(file_path):
        new_file_path = file_path + '/' + file_path.split('/')[-1] + '.asm'
    else:
        new_file_path = file_path.split('.')[0] + '.asm'
    save_file(new_file_path, asm_lines)


if __name__ == '__main__':
    translate()
