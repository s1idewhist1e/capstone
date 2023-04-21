
A simple, big endian computer with a 4-bit address space and and an 8 bit data space


## INSTRUCTIONS

### Definitions

#### Bit masks

`x`: ignored  
`c`: opcode  
`m`: operation msb  
`l`: operation lsb  

**NOP** - No operation  
  :   `0000 xxxx xxxx`  

### Memory Operations  

**STA [Address:4]** - Store register A at [Address]  
  :   `0001 mmmm xxxx`  

**STB [Address:4]** - Store register B at [Address]  
  :   `0010 mmmm xxxx`  

**LDA [Address:4]** - Load value at [Address] to register A  
  :   `0011 mmmm xxxx`  

**LDB [Address:4]** - Load value at [Address] to register B  
  :   `0100 mmmm xxxx`  

### Arithmetic Operations  

**SHL** - Shift A left by B amount -> A 
  :   `0101 xxxx xxxx`   
  **note:** only the 3 lsb will be used, rest will be ignored  

**SHR** - Shift A right by B amount -> A  
  :   `0110 xxxx xxxx`
  **note:** only the 3 lsb will be used, rest will be ignored

**AND** - Bitwise AND between A and B -> A  
  :   `0111 xxxx xxxx`  

**INV** - Bitwise completment of A -> A  
  :   `1000 xxxx xxxx`  

**INC** - Incrememnt A -> A  
  :   `1001 xxxx xxxx`  

### Register Operations

**LIA [Num:8]** - Load [Num] into A  
  :   `1010 mmmm llll`  

**LIB [Num:8]** - Load [Num] into B  
  :   `1011 mmmm llll`  

### Control Flow

**BNE** - Skip following instruction if A and B are not equal  
  :   `1100 xxxx xxxx`  

**JMP [Instruction:8]** - Jump to [Instruction]  
  :   `1101 mmmm llll`  

### Output

**OUT** - Display the value of A  
  :   `1110 xxxx xxxx`

## Structure

```
                          Main Bus
  /-----------------\       /==\       /--------------------------\
  | Program Counter | <===> |  | <===> | Accumulator (A Register) |
  \-----------------/       |  |       \--------------------------/ 
                            |  |                  /\  \/ 
  /-----------------\       |  |       /--------------------------\           
  | Address Register| <==== |  |       |            ALU           |
  \-----------------/       |  |       \--------------------------/           
          \/                |  |                    /\
  /-----------------\       |  |       /--------------------------\             
  |      RAM        | ====> |  | <===> |        B Register        |
  \-----------------/       |  |       \--------------------------/
                            |  | 
  /-----------------\       |  |       /--------------------------\
  | Address Register| <==== |  | ====> |      Output Register     |
  \-----------------/       |  |       \--------------------------/
          \/                |  | 
  /-----------------\       |  | 
  |       ROM       |       |  | 
  \-----------------/       |  | 
     \/         \/          |  |
  /------\   /------\       |  |
  |  Op  |   | Data | ====> |  |
  \------/   \------/       \==/
     \/
  /-----------------\     /----------------\
  | Instr. Decoder  | <=> | Instr. Counter |
  \-----------------/     \----------------/
    ||||||||||||||| Control Lines
```
