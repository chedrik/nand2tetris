//function Sys.init 0
(Sys.init)

//push constant 4000	
@4000	  // D=Val
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

//push constant 5000
@5000  // D=Val
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

//call Sys.main 0
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
@Sys.main // go to fcn 
0; JMP
(FCN_RETURN_1)

//pop temp 1
@1
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

//label LOOP
(LOOP)

//goto LOOP
@LOOP
0; JMP

//function Sys.main 5
(Sys.main)
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
@0  // D=Val
D=A
@SP  // *SP=D
A=M
M=D
@SP // SP++
M=M+1

//push constant 4001
@4001  // D=Val
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

//push constant 5001
@5001  // D=Val
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

//push constant 200
@200  // D=Val
D=A
@SP  // *SP=D
A=M
M=D
@SP // SP++
M=M+1

//pop local 1
@1
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

//push constant 40
@40  // D=Val
D=A
@SP  // *SP=D
A=M
M=D
@SP // SP++
M=M+1

//pop local 2
@2
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

//push constant 6
@6  // D=Val
D=A
@SP  // *SP=D
A=M
M=D
@SP // SP++
M=M+1

//pop local 3
@3
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

//push constant 123
@123  // D=Val
D=A
@SP  // *SP=D
A=M
M=D
@SP // SP++
M=M+1

//call Sys.add12 1
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
@Sys.add12 // go to fcn 
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

//push local 2
@2
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

//push local 3
@3
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

//push local 4
@4
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

//function Sys.add12 0
(Sys.add12)

//push constant 4002
@4002  // D=Val
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

//push constant 5002
@5002  // D=Val
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

//push constant 12
@12  // D=Val
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

