# IAS-in-Python
Implementation of the IAS architecture in Python

I have tried to implement the IAS architecture using Python.\
The IAS architecture includes registers like :\
1)AC (Accumalator) - Used to store calculation outputs\
2)MQ (Multiplication Quotient) - Used to store outputs of multiplication and division\
3)PC (Program counter)- Used to store the address of the instruction to be carried out\
4)MAR (Memory address register)- stores the instruction being carried out\
5)MBR (Memory buffer register)- stores the value (instruction/data) stored at the location MAR\
6)IR (Instruction register)- holds the op code of the current instruction\
7)IBR (Instruction buffer register)- stores the next instruction (right instruction) to be implemented next)\\



The following broad steps are followed as part of the cycle:\
1)Fetch -\
In this part of the cycle, PC loads the value of the next instruction and passes it to MAR. MBR loads the value stored at the location MAR.\

2)Decode - \
In this part of the cycle, IR loads the op code of the left instruction of the MBR, MAR loads the value of the address in the left instruction of MBR. IBR stores the right instruction from MBR.\

3)Execute - \
Depending on the op code stored in IR, the corresponding operation is carried out in the ALU, and the results are stored appropriately in AC and MQ. There are many operations which do not require the ALU; the respective instruction is carried out.\


Instructions used -\
1)load M(X)\
2)load MQ\
3)load |M(X)|\
4)add M(X)\
5)add |M(X)|\
6)stor M(X)\
7)sub M(X)\
8)div M(X)\\




The program I have tried to implement is a program to find the mean deviation of 5 numbers (1,2,3,4,5). The whole input to the function is hardcoded and does not require user input.\\

Assembly code for the program - \ 
load M(16) | add M(17)\
add M(18) | add M(19)\
add M(20) | stor M(21)\
load M(21) | div M(22)\
load MQ\
stor M(23) | load M(16)\
sub M(23) | stor M(24)\
load M(17) | sub M(23)\
stor M(25) | load M(18)\
sub M(23) | stor M(26)\
load M(19) | sub M(23)\
stor M(27) | load M(20)\
sub M(23) | stor M(28)\
load |M(24)| | add |M(25)|\
add |M(26)| | add |M(27)|\
add |M(28)| | div M(22)\
stor M(29) | halt\\


There are two functions bin_dec() and dec_bin() which convert binary to decimal and decimal to binary respectively used as tools along the way.\\

To run the program:\
Type - python3 IMT2021017_CA_assign_1.py on the terminal, in the directory that the file is in.
