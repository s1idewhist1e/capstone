


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
  :   `0002 mmmm xxxx`  

**LDA [Address:4]** - Load value at [Address] to register A  
  :   `0003 mmmm xxxx`  

**LDB [Address:4]** - Load value at [Address] to register B  
  :   `0004 mmmm xxxx`  

### Arithmetic Operations  

**SHL** - Shift A left by B amount  
  :   `0005 xxxx xxxx`   
  **note:** only the 3 lsb will be used, rest will be ignored  

**AND** - Bitwise AND between A and B  
  :   `0006 xxxx xxxx`  
