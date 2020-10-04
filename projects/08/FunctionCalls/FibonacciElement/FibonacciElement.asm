@256  // Sys init
D=A
@SP
M=D

@FCN_RETURN_1 // push return addr to label
D=A
@SP
A=M
M=D
@SP // SP++
M=M+1
@LCL // push LCL
D=M
@SP
A=M
M=D
@SP
M=M+1
@ARG // push ARG
D=M
@SP
A=M
M=D
@SP
M=M+1
@THIS // push THIS
D=M
@SP
A=M
M=D
@SP
M=M+1
@THAT // push THAT
D=M
@SP
A=M
M=D
@SP
M=M+1
@SP // ARG = SP-5-nAargs
D=M
@5
D=D-A
@ARG
M=D
@SP // LCL = SP 
D=M
@LCL
M=D
@Sys.init // go to fcn 
0; JMP
(FCN_RETURN_1)

//function Main.fibonacci 0
(Main.fibonacci)

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

//lt
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
D=M-D 
M=D 
@TRUE1 
D;JLT 
@R15 
M=0
(BACK1)
@R15  // D=Val
D=M
@SP  // *SP=D
A=M
M=D
@SP // SP++
M=M+1

//if-goto IF_TRUE
@SP // SP--
M=M-1
@SP
A=M
D=M
@IF_TRUE
D; JNE

//goto IF_FALSE
@IF_FALSE
0; JMP

//label IF_TRUE
(IF_TRUE)

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

//label IF_FALSE
(IF_FALSE)

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

//call Main.fibonacci 1
@FCN_RETURN_2 // push return addr to label
D=A
@SP
A=M
M=D
@SP // SP++
M=M+1
@LCL // push LCL
D=M
@SP
A=M
M=D
@SP
M=M+1
@ARG // push ARG
D=M
@SP
A=M
M=D
@SP
M=M+1
@THIS // push THIS
D=M
@SP
A=M
M=D
@SP
M=M+1
@THAT // push THAT
D=M
@SP
A=M
M=D
@SP
M=M+1
@SP // ARG = SP-5-nAargs
D=M
@6
D=D-A
@ARG
M=D
@SP // LCL = SP 
D=M
@LCL
M=D
@Main.fibonacci // go to fcn 
0; JMP
(FCN_RETURN_2)

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

//call Main.fibonacci 1
@FCN_RETURN_3 // push return addr to label
D=A
@SP
A=M
M=D
@SP // SP++
M=M+1
@LCL // push LCL
D=M
@SP
A=M
M=D
@SP
M=M+1
@ARG // push ARG
D=M
@SP
A=M
M=D
@SP
M=M+1
@THIS // push THIS
D=M
@SP
A=M
M=D
@SP
M=M+1
@THAT // push THAT
D=M
@SP
A=M
M=D
@SP
M=M+1
@SP // ARG = SP-5-nAargs
D=M
@6
D=D-A
@ARG
M=D
@SP // LCL = SP 
D=M
@LCL
M=D
@Main.fibonacci // go to fcn 
0; JMP
(FCN_RETURN_3)

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

//function Sys.init 0
(Sys.init)

//push constant 4
@4  // D=Val
D=A
@SP  // *SP=D
A=M
M=D
@SP // SP++
M=M+1

//call Main.fibonacci 1
@FCN_RETURN_4 // push return addr to label
D=A
@SP
A=M
M=D
@SP // SP++
M=M+1
@LCL // push LCL
D=M
@SP
A=M
M=D
@SP
M=M+1
@ARG // push ARG
D=M
@SP
A=M
M=D
@SP
M=M+1
@THIS // push THIS
D=M
@SP
A=M
M=D
@SP
M=M+1
@THAT // push THAT
D=M
@SP
A=M
M=D
@SP
M=M+1
@SP // ARG = SP-5-nAargs
D=M
@6
D=D-A
@ARG
M=D
@SP // LCL = SP 
D=M
@LCL
M=D
@Main.fibonacci // go to fcn 
0; JMP
(FCN_RETURN_4)

//label WHILE
(WHILE)

//goto WHILE
@WHILE
0; JMP

(END)  // infinite end-of-program loop
	@END
	0; JMP

(TRUE1) 
	@R15 
	M=-1 
	@BACK1
	0;JMP

