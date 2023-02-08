def dec_bin(a):   #function to convert decimal to binary
    if(type(a)==int):
        l=[]
        b=abs(a)
        if(a>=0):
            
            
           
            while(b>0):
                l.append(b%2)
                b=b//2
        else:
            while(b>0):
                if(b%2==0):
                    l.append(1)
                else:
                    l.append(0)
                b=b//2
    
        
        if(a<0):   #for negative numbers
            i=0
            while(l[i]==1):
                l[i]=0
                i=i+1
            l[i]=1



        l.reverse()
    
    

        st = "".join([str(ele) for ele in l]) 
        if(a<0):
            return st.rjust(40, '1') 
        else:  
            return st.zfill(40)
    else:
        return a


def bin_dec(a):   #function to convert binary to decimal
    if(type(a)==str):
        dec=0
        a=str(a)
        if(a[0]=='1'):
            dec=dec-(2**(len(a)-1))
            for i in range(1,len(a)):
                dec=dec+int(a[i])*(2**(len(a)-i-1))

        else:
        
        
            for i in range(len(a)):
                dec=dec+int(a[i])*(2**(len(a)-i-1))
        return dec
    else:
        return a


a=0     #used to indicate that the next instruction should be fetched when a is incremented
ac=0    #accumalator
mq=0    #MQ
ibr=0   #instruction buffer register
ir=0    #Instruction register
mbr=0   #Memory buffer register
pc=0    #Program counter
mar=0   #Memory address register

add=[]   #list to store addreses
mem=[]   #list to store corresponding memory values

def input1():
    #These instructions find the mean deviation of numbers from memory locations 16 to 20
    #first 10 instructions to find the average of 5 numbers.(left and right instruction considered seperately)
    #next set of instructions to find the absolute value of the difference of each number (location 16 to 20) with the average
    #next set is to find the average of the absolute values of the differences calcualted in the previous steps
    #This is followed by the data used in the program and the spaces to store future calculations


    mem.append("0000000100000001000000000101000000010001")   #load M(16) | add M(17)
    mem.append("0000010100000001001000000101000000010011")   #add M(18) | add M(19)
    mem.append("0000010100000001010000100001000000010101")   #add M(20) | stor M(21)
    mem.append("0000000100000001010100001100000000010110")   #load M(21) | div M(22)
    mem.append("00001010")                                   #load MQ   
    mem.append("0010000100000001011100000001000000010000")   #stor M(23) | load M(16)
    mem.append("0000011000000001011100100001000000011000")   #sub M(23) | stor M(24)
    mem.append("0000000100000001000100000110000000010111")   #load M(17) | sub M(23)
    mem.append("0010000100000001100100000001000000010010")   #stor M(25) | load M(18)
    mem.append("0000011000000001011100100001000000011010")   #sub M(23) | stor M(26)
    mem.append("0000000100000001001100000110000000010111")   #load M(19) | sub M(23)
    mem.append("0010000100000001101100000001000000010100")   #stor M(27) | load M(20)
    mem.append("0000011000000001011100100001000000011100")   #sub M(23) | stor M(28)
    mem.append("0000001100000001100000000111000000011001")   #load |M(24)| | add |M(25)|
    mem.append("0000011100000001101000000111000000011011")   #add |M(26)| | add |M(27)|
    mem.append("0000011100000001110000001100000000010110")   #add |M(28)| | div M(22)
    mem.append("0010000100000001110100000000000000000000")   # stor M(29) | halt  , 20 0's indicates halt (right instruction)
    mem.append(1)   #data values
    mem.append(2)
    mem.append(3)
    mem.append(4)
    mem.append(5)
    mem.append(6)
    mem.append(5)
    mem.append(8)
    mem.append(9)
    mem.append(10)
    mem.append(11)
    mem.append(12)
    mem.append(13)
    mem.append(14)



    add.append("000000000000")  #addresses
    add.append("000000000001")
    add.append("000000000010")
    add.append("000000000011")
    add.append("000000000100")
    add.append("000000000101")
    add.append("000000000110")
    add.append("000000000111")
    add.append("000000001000")
    add.append("000000001001")
    add.append("000000001010")
    add.append("000000001011")
    add.append("000000001100")
    add.append("000000001101")
    add.append("000000001110")
    add.append("000000001111")
    add.append("000000011110")   
    add.append("000000010000")
    add.append("000000010001")
    add.append("000000010010")
    add.append("000000010011")
    add.append("000000010100")
    add.append("000000010101")
    add.append("000000010110")
    add.append("000000010111")
    add.append("000000011000")
    add.append("000000011001")
    add.append("000000011010")
    add.append("000000011011")
    add.append("000000011100")
    add.append("000000011101")
    








def execute():   #execute part of the cycle
    global mbr
    global mar
    global ac
    global ir
    global ibr
    global a
    global mq
    s=ir                    #checking the op codes to know the instruction to be performed
    if(s=="00000000"):   #halt
        exit()
    if(s=="00000001"):   #load M(X)
        
        ac=mem[add.index(mar)]

        
    if(s=="00100001"):    #stor M(X)
        mem[add.index(mar)]=ac
        
    if(s=="00000101"):    #add M(X)
        ac=bin_dec(ac)+bin_dec(mem[add.index(mar)])
        #ac=dec_bin(ac)
    if(s=="00000011"):    # load |M(X)|
        
        ac=abs(bin_dec(mem[add.index(mar)]))
        #ac=dec_bin(ac)
    if(s=="00000111"):    #add |M(X)|
        ac=bin_dec(ac)+abs(int(mem[add.index(mar)]))
        #ac=dec_bin(ac)
    if(s=="00001010"):   #load MQ
        ac=mq
    if(s=="00000110"):    #sub M(X)
        ac=bin_dec(ac)-int(mem[add.index(mar)])
        #ac=dec_bin(ac)
    if(s=="00001100"):    #div M(X)
        mq=bin_dec(ac)//int(mem[add.index(mar)])
        ac=bin_dec(ac)%int(mem[add.index(mar)])
        #mq=dec_bin(mq)
        #ac=dec_bin(ac)
    
    
    if(ibr!=0):
        mar=ibr[8:20]
        ir=ibr[0:8]
        ibr=0
        execute()
    else:
        a=a+1

        fetch()    
    
    
    
    













def decode():   #decode part of the cycle
    global mar
    global mbr
    global ibr
    global ir
    global pc

    

    ir=mbr[0:8]
    pc=mbr[8:20]
    mar=pc
    if(len(mbr)==40):
        ibr=mbr[20:40]
    else:
        ibr=0
    execute()






def fetch():   #fetch part of the cycle
    global pc
    global ibr
    global mar
    global mbr
    global a
    mar=pc
    mbr=mem[a]
    decode()



input1()   #calling the input function to assign values in the memory

pc=add[0]   #initializing pc
fetch()        #fetching an instruction









