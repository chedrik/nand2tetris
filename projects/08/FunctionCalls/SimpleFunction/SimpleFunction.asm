//function SimpleFunction.test 2
(SimpleFunction.test)
@0  // D=Val
D=A
@SP  // *SP=D
A=M
M=D
@SP // SP++
M=M+1
@0  // D=Val
D=A
@SP  // *SP=D
A=M
M=D
@SP // SP++
M=M+1

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

//push local 1
@1
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

//not
@SP // SP--
M=M-1
@SP
A=M
D=M
@R15
M=D
@R15
M=!M
@R15  // D=Val
D=M
@SP  // *SP=D
A=M
M=D
@SP // SP++
M=M+1

//push argument 0
@0
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

//return
@LCL // endframe=LCL 
D=M
@FRAME
M=D
@FRAME // set retaddr 
D=M
@5
D=D-A
A=D
D=M
@RET
M=D
@0
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
@ARG // SP = ARG + 1
D=M+1
@SP
M=D
@FRAME // set THAT 
D=M
@1
D=D-A
A=D
D=M
@THAT
M=D
@FRAME // set THIS 
D=M
@2
D=D-A
A=D
D=M
@THIS
M=D
@FRAME // set ARG 
D=M
@3
D=D-A
A=D
D=M
@ARG
M=D
@FRAME // set LCL 
D=M
@4
D=D-A
A=D
D=M
@LCL
M=D
@RET // goto ret 
A=M
0; JMP

(END)  // infinite end-of-program loop
	@END
	0; JMP

