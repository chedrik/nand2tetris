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

//function Class1.set 0
(Class1.set)

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

//pop static 0
@SP // SP--
M=M-1
@SP
A=M
D=M
@Class1.0
M=D

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

//pop static 1
@SP // SP--
M=M-1
@SP
A=M
D=M
@Class1.1
M=D

//push constant 0
@0  // D=Val
D=A
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

//function Class1.get 0
(Class1.get)

//push static 0
@Class1.0
D=M
@SP  // *SP=D
A=M
M=D
@SP // SP++
M=M+1

//push static 1
@Class1.1
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

//push constant 6
@6  // D=Val
D=A
@SP  // *SP=D
A=M
M=D
@SP // SP++
M=M+1

//push constant 8
@8  // D=Val
D=A
@SP  // *SP=D
A=M
M=D
@SP // SP++
M=M+1

//call Class1.set 2
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
@7
D=D-A
@ARG
M=D
@SP // LCL = SP 
D=M
@LCL
M=D
@Class1.set // go to fcn 
0; JMP
(FCN_RETURN_2)

//pop temp 0
@0
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

//push constant 23
@23  // D=Val
D=A
@SP  // *SP=D
A=M
M=D
@SP // SP++
M=M+1

//push constant 15
@15  // D=Val
D=A
@SP  // *SP=D
A=M
M=D
@SP // SP++
M=M+1

//call Class2.set 2
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
@7
D=D-A
@ARG
M=D
@SP // LCL = SP 
D=M
@LCL
M=D
@Class2.set // go to fcn 
0; JMP
(FCN_RETURN_3)

//pop temp 0
@0
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

//call Class1.get 0
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
@5
D=D-A
@ARG
M=D
@SP // LCL = SP 
D=M
@LCL
M=D
@Class1.get // go to fcn 
0; JMP
(FCN_RETURN_4)

//call Class2.get 0
@FCN_RETURN_5 // push return addr to label
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
@Class2.get // go to fcn 
0; JMP
(FCN_RETURN_5)

//label WHILE
(WHILE)

//goto WHILE
@WHILE
0; JMP

//function Class2.set 0
(Class2.set)

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

//pop static 0
@SP // SP--
M=M-1
@SP
A=M
D=M
@Class2.0
M=D

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

//pop static 1
@SP // SP--
M=M-1
@SP
A=M
D=M
@Class2.1
M=D

//push constant 0
@0  // D=Val
D=A
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

//function Class2.get 0
(Class2.get)

//push static 0
@Class2.0
D=M
@SP  // *SP=D
A=M
M=D
@SP // SP++
M=M+1

//push static 1
@Class2.1
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

