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

//pop pointer 1
@SP // SP--
M=M-1
@SP
A=M
D=M
@THAT
M=D

//push constant 0
@0  // D=Val
D=A
@SP  // *SP=D
A=M
M=D
@SP // SP++
M=M+1

//pop that 0
@0
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

//push constant 1
@1  // D=Val
D=A
@SP  // *SP=D
A=M
M=D
@SP // SP++
M=M+1

//pop that 1
@1
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

//push constant 2
@2  // D=Val
D=A
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

//pop argument 0
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

//label MAIN_LOOP_START
(MAIN_LOOP_START)

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

//if-goto COMPUTE_ELEMENT
@SP // SP--
M=M-1
@SP
A=M
D=M
@COMPUTE_ELEMENT
D; JNE

//goto END_PROGRAM
@END_PROGRAM
0; JMP

//label COMPUTE_ELEMENT
(COMPUTE_ELEMENT)

//push that 0
@0
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

//push that 1
@1
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

//push pointer 1
@THAT
D=M
@SP  // *SP=D
A=M
M=D
@SP // SP++
M=M+1

//push constant 1
@1  // D=Val
D=A
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

//pop pointer 1
@SP // SP--
M=M-1
@SP
A=M
D=M
@THAT
M=D

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

//push constant 1
@1  // D=Val
D=A
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

//pop argument 0
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

//goto MAIN_LOOP_START
@MAIN_LOOP_START
0; JMP

//label END_PROGRAM
(END_PROGRAM)

(END)  // infinite end-of-program loop
	@END
	0; JMP

