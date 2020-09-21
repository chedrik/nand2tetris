//push constant 3030
@3030  // D=Val
D=A
@SP  // *SP=D
A=M
M=D
@SP // SP++
M=M+1

//pop pointer 0
@SP // SP--
M=M-1
@SP
A=M
D=M
@THIS
M=D

//push constant 3040
@3040  // D=Val
D=A
@SP  // *SP=D
A=M
M=D
@SP // SP++
M=M+1

//pop pointer 1
@SP // SP--
M=M-1
@SP
A=M
D=M
@THAT
M=D

//push constant 32
@32  // D=Val
D=A
@SP  // *SP=D
A=M
M=D
@SP // SP++
M=M+1

//pop this 2
@2
D=A
@THIS
D=D+M
@R13
M=D
@SP // SP--
M=M-1
@SP
A=M
D=M
@R13
A=M
M=D

//push constant 46
@46  // D=Val
D=A
@SP  // *SP=D
A=M
M=D
@SP // SP++
M=M+1

//pop that 6
@6
D=A
@THAT
D=D+M
@R13
M=D
@SP // SP--
M=M-1
@SP
A=M
D=M
@R13
A=M
M=D

//push pointer 0
@THIS
D=M
@SP  // *SP=D
A=M
M=D
@SP // SP++
M=M+1

//push pointer 1
@THAT
D=M
@SP  // *SP=D
A=M
M=D
@SP // SP++
M=M+1

//add
@SP // SP--
M=M-1
@SP
A=M
D=M
@R14
M=D
@SP // SP--
M=M-1
@SP
A=M
D=M
@R15
M=D
@R14
D=M
@R15
M=D+M
@R15  // D=Val
D=M
@SP  // *SP=D
A=M
M=D
@SP // SP++
M=M+1

//push this 2
@2
D=A
@THIS
D=D+M
@R13
M=D
@R13
A=M
D=M
@SP
A=M
M=D
@SP // SP++
M=M+1

//sub
@SP // SP--
M=M-1
@SP
A=M
D=M
@R14
M=D
@SP // SP--
M=M-1
@SP
A=M
D=M
@R15
M=D
@R14
D=M
@R15
M=M-D
@R15  // D=Val
D=M
@SP  // *SP=D
A=M
M=D
@SP // SP++
M=M+1

//push that 6
@6
D=A
@THAT
D=D+M
@R13
M=D
@R13
A=M
D=M
@SP
A=M
M=D
@SP // SP++
M=M+1

//add
@SP // SP--
M=M-1
@SP
A=M
D=M
@R14
M=D
@SP // SP--
M=M-1
@SP
A=M
D=M
@R15
M=D
@R14
D=M
@R15
M=D+M
@R15  // D=Val
D=M
@SP  // *SP=D
A=M
M=D
@SP // SP++
M=M+1

