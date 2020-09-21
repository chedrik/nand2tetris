//push constant 17
@17  // D=Val
D=A
@SP  // *SP=D
A=M
M=D
@SP // SP++
M=M+1

//push constant 17
@17  // D=Val
D=A
@SP  // *SP=D
A=M
M=D
@SP // SP++
M=M+1

//eq
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
D;JEQ
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

//push constant 17
@17  // D=Val
D=A
@SP  // *SP=D
A=M
M=D
@SP // SP++
M=M+1

//push constant 16
@16  // D=Val
D=A
@SP  // *SP=D
A=M
M=D
@SP // SP++
M=M+1

//eq
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
@TRUE2
D;JEQ
@R15
M=0
(BACK2)
@R15  // D=Val
D=M
@SP  // *SP=D
A=M
M=D
@SP // SP++
M=M+1

//push constant 16
@16  // D=Val
D=A
@SP  // *SP=D
A=M
M=D
@SP // SP++
M=M+1

//push constant 17
@17  // D=Val
D=A
@SP  // *SP=D
A=M
M=D
@SP // SP++
M=M+1

//eq
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
@TRUE3
D;JEQ
@R15
M=0
(BACK3)
@R15  // D=Val
D=M
@SP  // *SP=D
A=M
M=D
@SP // SP++
M=M+1

//push constant 892
@892  // D=Val
D=A
@SP  // *SP=D
A=M
M=D
@SP // SP++
M=M+1

//push constant 891
@891  // D=Val
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
@TRUE4 
D;JLT 
@R15 
M=0
(BACK4)
@R15  // D=Val
D=M
@SP  // *SP=D
A=M
M=D
@SP // SP++
M=M+1

//push constant 891
@891  // D=Val
D=A
@SP  // *SP=D
A=M
M=D
@SP // SP++
M=M+1

//push constant 892
@892  // D=Val
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
@TRUE5 
D;JLT 
@R15 
M=0
(BACK5)
@R15  // D=Val
D=M
@SP  // *SP=D
A=M
M=D
@SP // SP++
M=M+1

//push constant 891
@891  // D=Val
D=A
@SP  // *SP=D
A=M
M=D
@SP // SP++
M=M+1

//push constant 891
@891  // D=Val
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
@TRUE6 
D;JLT 
@R15 
M=0
(BACK6)
@R15  // D=Val
D=M
@SP  // *SP=D
A=M
M=D
@SP // SP++
M=M+1

//push constant 32767
@32767  // D=Val
D=A
@SP  // *SP=D
A=M
M=D
@SP // SP++
M=M+1

//push constant 32766
@32766  // D=Val
D=A
@SP  // *SP=D
A=M
M=D
@SP // SP++
M=M+1

//gt
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
@TRUE7
D;JGT
@R15
M=0
(BACK7)
@R15  // D=Val
D=M
@SP  // *SP=D
A=M
M=D
@SP // SP++
M=M+1

//push constant 32766
@32766  // D=Val
D=A
@SP  // *SP=D
A=M
M=D
@SP // SP++
M=M+1

//push constant 32767
@32767  // D=Val
D=A
@SP  // *SP=D
A=M
M=D
@SP // SP++
M=M+1

//gt
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
@TRUE8
D;JGT
@R15
M=0
(BACK8)
@R15  // D=Val
D=M
@SP  // *SP=D
A=M
M=D
@SP // SP++
M=M+1

//push constant 32766
@32766  // D=Val
D=A
@SP  // *SP=D
A=M
M=D
@SP // SP++
M=M+1

//push constant 32766
@32766  // D=Val
D=A
@SP  // *SP=D
A=M
M=D
@SP // SP++
M=M+1

//gt
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
@TRUE9
D;JGT
@R15
M=0
(BACK9)
@R15  // D=Val
D=M
@SP  // *SP=D
A=M
M=D
@SP // SP++
M=M+1

//push constant 57
@57  // D=Val
D=A
@SP  // *SP=D
A=M
M=D
@SP // SP++
M=M+1

//push constant 31
@31  // D=Val
D=A
@SP  // *SP=D
A=M
M=D
@SP // SP++
M=M+1

//push constant 53
@53  // D=Val
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

//push constant 112
@112  // D=Val
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

//neg
@SP // SP--
M=M-1
@SP
A=M
D=M
@R15
M=D
@R15
M=-M
@R15  // D=Val
D=M
@SP  // *SP=D
A=M
M=D
@SP // SP++
M=M+1

//and
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
M=D&M
@R15  // D=Val
D=M
@SP  // *SP=D
A=M
M=D
@SP // SP++
M=M+1

//push constant 82
@82  // D=Val
D=A
@SP  // *SP=D
A=M
M=D
@SP // SP++
M=M+1

//or
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
M=D|M
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

(END)  // infinite end-of-program loop
	@END
	0; JMP

(TRUE1) 
	@R15 
	M=-1 
	@BACK1
	0;JMP

(TRUE2) 
	@R15 
	M=-1 
	@BACK2
	0;JMP

(TRUE3) 
	@R15 
	M=-1 
	@BACK3
	0;JMP

(TRUE4) 
	@R15 
	M=-1 
	@BACK4
	0;JMP

(TRUE5) 
	@R15 
	M=-1 
	@BACK5
	0;JMP

(TRUE6) 
	@R15 
	M=-1 
	@BACK6
	0;JMP

(TRUE7) 
	@R15 
	M=-1 
	@BACK7
	0;JMP

(TRUE8) 
	@R15 
	M=-1 
	@BACK8
	0;JMP

(TRUE9) 
	@R15 
	M=-1 
	@BACK9
	0;JMP

