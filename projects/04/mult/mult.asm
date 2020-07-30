// This file is part of www.nand2tetris.org
// and the book "The Elements of Computing Systems"
// by Nisan and Schocken, MIT Press.
// File name: projects/04/Mult.asm

// Multiplies R0 and R1 and stores the result in R2.
// (R0, R1, R2 refer to RAM[0], RAM[1], and RAM[2], respectively.)

// Put your code here.

@i 
M=0  // i = 0
@R2
M=0  // R2 = 0

(LOOP)
    @i
    D=M  // D=i

    @R1
    D=D-M // D=i-RAM[1]

    @END
    D;JGE  // If i-R1 >0, end

    @R0
    D=M
    @R2
    M=D+M


    @i
    M=M+1  // i++

    @LOOP
    0;JMP // Goto loop
    
(END)  // infinite end-of-program loop
    @END
    0; JMP
