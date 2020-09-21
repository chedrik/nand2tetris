//push constant 10
@10  // D=Val
D=A
@SP  // *SP=D
A=M
M=D
@SP // SP++
M=M+1

//pop local 0
@0
D=A
@LCL
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

//push constant 21
@21  // D=Val
D=A
@SP  // *SP=D
A=M
M=D
@SP // SP++
M=M+1

//push constant 22
@22  // D=Val
D=A
@SP  // *SP=D
A=M
M=D
@SP // SP++
M=M+1

//pop argument 2
@2
D=A
@ARG
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

//pop argument 1
@1
D=A
@ARG
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

//push constant 36
@36  // D=Val
D=A
@SP  // *SP=D
A=M
M=D
@SP // SP++
M=M+1

//pop this 6
@6
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

//push constant 42
@42  // D=Val
D=A
@SP  // *SP=D
A=M
M=D
@SP // SP++
M=M+1

//push constant 45
@45  // D=Val
D=A
@SP  // *SP=D
A=M
M=D
@SP // SP++
M=M+1

//pop that 5
@5
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

//pop that 2
@2
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

//push constant 510
@510  // D=Val
D=A
@SP  // *SP=D
A=M
M=D
@SP // SP++
M=M+1

//pop temp 6
@6
D=A
@5
D=D+A
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

//push local 0
@0
D=A
@LCL
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

//push that 5
@5
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

//push argument 1
@1
D=A
@ARG
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

//push this 6
@6
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

//push this 6
@6
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

//push temp 6
@6
D=A
@5
D=D+A
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

