import random as r
    
def int_input(message, low, high):
    print("")
    try:
        stuff = int(input(message))
        if stuff > low and stuff < high:
            return stuff
        else:
            print("number between", low+1,"and", high-1)
            return int_input("input error\nenter a number: ",low,high)
    except:
        return int_input("input error\nenter a number: ",low,high)


print("")
print("-----BinDec Training-----\n\n1: Random \n2: Dec-Bin \n3: Bin-Dec")
m=2
Mode = int_input("Mode:", 0,4)
Rounds = int_input("Rounds:",0,100)
Range = int_input("Range:",0,8193)
rate_r=0
rate_d_b = 0
rate_b_d = 0
    
for ro in range(0, Rounds):
    print("---------------------------")
    print("Round:", ro+1)
    win=False
    ZahlDec = r.randint(0, Range)
    ZahlBin = format(ZahlDec, "b")
    
    if Mode == 1:
        m = r.randint(0,1)
    if Mode == 2:
        m = 0
    if Mode == 3:
            m = 1
        
    if m==0:
        print("Dec:", ZahlDec)
        ZahlGuess = int_input("Bin: ",-1,10000000000001)
        if format(ZahlGuess, "d") == ZahlBin:
            win=True
    if m==1:
        print("Bin:", ZahlBin)
        ZahlGuess = int_input("Dec: ",-1,8193)
        if ZahlGuess == ZahlDec:
            win=True
        
    print(win)
    if win:
        rate_r=rate_r+1
    else:
        print("Dec:", ZahlDec,"Bin:", ZahlBin)
        

rate_r = 100*rate_r/Rounds
print("_____")
print("")
print("Right to", rate_r, "%")
print("-----------------END")      
        
    
    
