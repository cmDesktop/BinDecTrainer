import random as r
    
print("")
print("-----BinDec Training-----\n\n1: Random \n2: Dec-Bin \n3: Bin-Dec")
m=2

inputsCorrect = False
while (inputsCorrect == False):
    Mode = input("Mode:")
    if(Mode != ""):
        Mode = int(Mode)
        inputsCorrect = True
    else: print("input error")

inputsCorrect = False
while (inputsCorrect == False):
    Rounds = input("Rounds:")
    if(Rounds != ""):
        Rounds = int(Rounds)
        inputsCorrect = True
    else: print("input error")

inputsCorrect = False
while (inputsCorrect == False):
    Range = input("Range:")
    if(Range != ""):
        Range = int(Range)
        inputsCorrect = True
    else: print("input error")

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
        inputsCorrect = False
        while (inputsCorrect == False):
            ZahlGuess = input("Bin: ")
            if(ZahlGuess != ""):
                ZahlGuess = int(ZahlGuess) 
                inputsCorrect = True      
                if format(ZahlGuess, "d") == ZahlBin:
                    win=True
            else: print("input error")
    if m==1:
        print("Bin:", ZahlBin)
        inputsCorrect = False
        while (inputsCorrect == False):
            ZahlGuess = input("Dec: ")
            if(ZahlGuess != ""):
                ZahlGuess = int(ZahlGuess)   
                inputsCorrect = True  
                if ZahlGuess == ZahlDec:
                    win=True
            else: print("input error")
        
    print(win)
    if win:
        rate_r=rate_r+1
    else:
        print("Dec:", ZahlDec,"Bin:", ZahlBin)
        

rate_r = 100*rate_r/Rounds
print("_____")
print("")
print("Round:", rate_r, "%")
print("-----------------END")      
        
    
    
