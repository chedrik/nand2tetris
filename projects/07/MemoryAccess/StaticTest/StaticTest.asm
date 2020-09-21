//push constant 111
@111  // D=Val
D=A
@SP  // *SP=D
A=M
M=D
@SP // SP++
M=M+1

//push constant 333
@333  // D=Val
D=A
@SP  // *SP=D
A=M
M=D
@SP // SP++
M=M+1

//push constant 888
@888  // D=Val
D=A
@SP  // *SP=D
A=M
M=D
@SP // SP++
M=M+1

//pop static 8
@SP // SP--
M=M-1
@SP
A=M
D=M
@StaticTest.8
M=D

//pop static 3
@SP // SP--
M=M-1
@SP
A=M
D=M
@StaticTest.3
M=D

//pop static 1
@SP // SP--
M=M-1
@SP
A=M
D=M
@StaticTest.1
M=D

//push static 3
@StaticTest.3
D=M
@SP  // *SP=D
A=M
M=D
@SP // SP++
M=M+1

//push static 1
@StaticTest.1
D=M
@SP  // *SP=D
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

//push static 8
@StaticTest.8
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

