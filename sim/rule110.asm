; Rule 110

	LIA 0x1 ; starts with 0b00000001
	STA 0x0 ; main field
	LIA 0x6E ; load 110 (0x6E) into memory
	STA 0x1
main:
	LDA 0x0
	OUT
	LIA 0x0 
	STA 0xE ; counter
	STA 0x2 ; new field

	LDA 0x0
	LIB 0x1
	SHL
	STA 0x3 ; alt field

loop:   
	LDA 0x3 ; load alt field
	LIB 0x7
	AND ; mask with lowest 3 bits
	STA 0xF
	LDB 0xF
	LDA 0x1 ; load 110
	SHR
	LIB 0x1
	AND ; mask to n'th bit of 110
	
	LDB 0xE ; load counter
	SHL
	INV ; DeMorgans law to allow for OR using AND
	STA 0xF
	LDB 0xF
	LDA 0x2
	INV
	AND
	INV
	STA 0x2

	; increment counter
	LDA 0xE
	INC
	
	; check if necessary to continue loop
	LIB 0x8
	BNE
	JMP loop_end
	STA 0xE ; store counter
	LDA 0x3
	LIB 0x1
	SHR
	STA 0x3
	JMP loop 
	
loop_end:
	LDA 0x2
	STA 0x0
	
	JMP main

