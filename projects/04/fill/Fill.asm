// This file is part of www.nand2tetris.org
// and the book "The Elements of Computing Systems"
// by Nisan and Schocken, MIT Press.
// File name: projects/04/Fill.asm

// Runs an infinite loop that listens to the keyboard input.
// When a key is pressed (any key), the program blackens the screen,
// i.e. writes "black" in every pixel;
// the screen should remain fully black as long as the key is pressed. 
// When no key is pressed, the program clears the screen, i.e. writes
// "white" in every pixel;
// the screen should remain fully clear as long as no key is pressed.

// Put your code here.


@SCREEN
D=A
@addr
M=D // screen base address

@8192
D=A
@n      // end of screen
M=D

@i
M=0  //i = 0

(WAIT)  // Do nothing and wait for kbd
    @KBD
    D=M
    @FILL
    D;JGT  // If kbd -> FILL

    @WHITE
    0;JMP

(FILL)
    @i
    D=M  // D=i
    @n
    D=D-M
    @WAIT
    D;JEQ  // If screen full, go to wait

    @KBD
    D=M
    @WHITE
    D;JEQ  // If not kbd -> WHITE

    @addr
    A=M
    M=-1 // sets RAM[addr] to all 1s

    @i
    M=M+1

    @32
    D=A
    @addr
    M=M+1
    
    @FILL
    0;JMP // Keep filling

(WHITE)
    @i
    D=M  // D=i
    @WAIT
    D;JLT  // If screen empty, go to wait

    @KBD
    D=M
    @FILL
    D;JGT  // If kbd -> FILL

    @addr
    A=M
    M=0 // sets RAM[addr] to all 0s

    @i
    M=M-1

    @32
    D=A
    @addr
    M=M-1
    
    @WHITE
    0;JMP // Keep erasing