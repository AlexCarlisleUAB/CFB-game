import random
def CoinToss():
    userCoin = input("Time for the coin toss: Please select Heads(1) or Tails(2).")
    
    while userCoin != 1 or userCoin != 2:                                                       #Coin selection error handling
        print("Error! Please only select 1 for heads, 2 for tails!")
        userCoin = input()
    
    poss = False
    plays = random.randint(100, 125) 
    coin = random.randint(1,2)
    if coin == userCoin:                                                                        #if user wins the toss
        kickoffChoice = input("you have won the toss! Receive(1) or Kick(2)?")
        while kickoffChoice != 1 or kickoffChoice != 2:                                         #User kickoff selection error handling
            print("Error! Please only select 1 or 2!")
            kickoffChoice = input()
        if kickoffChoice == 1:                                                                  #if user selects receive
            Kickoff(poss, 0, 0)
        elif kickoffChoice == 2:                                                                #if user selects kick
            poss = True
            Kickoff(poss, 0, 0, plays)
    else:                                                                                       #if CPU wins toss
        kC = random.randint(1,2)
        if kC == 1:                                                                             #CPU selects receive
            poss = True
            Kickoff(poss, 0, 0)
        elif kickoffChoice == 2:                                                                #CPU selects kick
            Kickoff(poss, 0, 0)
        
            

def Kickoff(poss, userScore, oppScore, plays):
    print("Kicking off...")
    poss = not poss #flipping possession 
    startingPos = 35 #starting distance for kickoffs
    kickDist = random.randint(50,75) #kicking off, randomly generating kick distance
    startingFP = 0 #establishing starting field position
    if kickDist >= 65:                                                                          #touchback
        startingFP = 25
        print("Touchback.")
    else:                                                                                       #normal kick return
        kickCatch = 100 - startingPos + kickDist
        kickRet = random.randint(13,26)
        if kickRet == 26:                                                                       #BIG KICK RETURN POSSIBILITY
            print("BIG RETURN!")
            kickRet = random.randint(26,99)
            if kickCatch + kickRet >= 100:                                                      #If the kick is returned for TD
                print("Touchdown!")
                if poss == True:                                                                #If it was the user that returned the kick for TD
                    userScore = userScore + 6
                    ExtraPoint(poss, userScore, oppScore)
                else:                                                                           #If it was the CPU that returned the kick for TD
                    oppScore = oppScore + 6
                    ExtraPoint(poss, userScore, oppScore)
        startingFP = kickCatch + kickRet                                                        #if return is not a TD, setting starting field position
    Drive(poss, userScore, oppScore, startingFP)

def Drive(poss, userScore, oppScore, startingFP, plays):
    down = 1 #1st down
    yardsToGo = 10 #ten yards to go
    fp = startingFP #setting field position
    while poss == True: 
        print("It is ", down, " down and ", yardsToGo)
        playcall = input("Run(1), Pass(2), Punt(3), or Kick a FG(4)?")
        if playcall == 1:
            yards = Run(poss, userScore, oppScore, fp)
            fp = fp + yards
        elif playcall == 2:
            yards = Pass(poss, userScore, oppScore, fp)
            fp = fp + yards
        elif playcall == 3:
            Punt(poss, userScore, oppScore, fp)
        elif playcall == 4:
            FG(poss, userScore, oppScore, fp)
        if yards < yardsToGo:
            yardsToGo = yardsToGo - yards
            down = down + 1
        if down == 5:
            poss = not poss
            fp = 100 - fp
            Drive(poss, userScore, oppScore, fp)
    while poss == False:
        print("It is ", down, " down and ", yardsToGo)
        if down != 4:
            playcall = random.randint(1,2)
            if playcall == 1:
                yards = Run(poss, userScore, oppScore, fp)
                fp = fp + yards
            elif playcall == 2:
                yards = Pass(poss, userScore, oppScore, fp)
                fp = fp + yards
        
            
    
    #todo

def Run(poss, userScore, oppScore, fp):
    runYd = random.randint(-3, 11)                                                              #initial rushing yards
    if runYd == 11:                                                                             #Big gain rush yards
        runYd = random.randint(11, 99)
    return runYd

def Pass(poss, userScore, oppScore, fp):
    passYd = random.randint(-8, 26)
    passCmp = random.randint(1, 100)
    if passCmp > 66:                                                                            #incomplete pass
        passYd = 0
        print("Incomplete Pass!")
    elif passYd == 26:                                                                          #big pass
        passYd = random.randint(26,99)
    elif passCmp == 66:
        print ("Interception")                                                                  #interception
        poss = not poss #change possession
        fp = passYd + fp #adding yards on from where the int was caught
        fp = 100 - fp #flipping field position value due to change in possession  
    elif passYd < 0:                                                                            #sacked
        print("Sacked!")
    return passYd

def Punt(poss, userScore, oppScore, fp, plays):
    puntYds = random.randint(40, 55)
    fp = puntYds + fp
    puntRet = 0
    if fp > 100:                                                                                #if field position of punt + punt yards > 100, its a touchback
        print("touchback")
        fp = 25
    else:                                                                                       #else flip field position value
        fp = 100 - fp
        puntRetChance = random.randint(1,2)
        if puntRetChance == 2:                                                                  #if punt is returned, get yardage value 0-16
            puntRet = random.randint(0, 16)
            if puntRet == 16:                                                                   #Big punt return
                puntRet = random.randint(16, 100)
    poss = not poss
    plays = plays - 1
    if plays > 0:
        Drive(poss, userScore, oppScore, fp, plays)
    
def FG(poss, userScore, oppScore, fp):
    fgChance = 0
    fgAtt = random.randint(0,100) 
    if fp < 65:                                                                                 #if kick attempt is too far out
        print("Field goal missed! Way out of range!")
        poss = not poss
        Kickoff(poss, userScore, oppScore)
    if fp < 70:                                                                                 #if kick is in 30-35 range
        fgChance = 40
    elif fp < 75:                                                                               #if kick is in 25-30 range
        fgChance = 60
    elif fp < 80:                                                                               #if kick is in 20-25 range
        fgChance = 75
    elif fp < 90:                                                                               #if kick is in 10-20 range
        fgChance = 85
    else:                                                                                       #if kick is within 10 yards
        fgChance = 90
    if fgChance > fgAtt:
        if poss == True:
            print("FG GOOD!")
            userScore = userScore + 3
        else:
            print("Opponent FG GOOD!")
            oppScore = oppScore + 3
    else:
        print("FG Missed! Score still the same!")
             
    
def ExtraPoint(poss, userScore, oppScore):
    kickMake = 97
    xpAtt = random.randint(1,100)
    if xpAtt <= kickMake:
        print("Extra Point is good!")
        if poss == True:                                                                        #If user made the PAT
            userScore = userScore + 1
        else:                                                                                   #If CPU made PAT
            oppScore = oppScore + 1
    else:                                                                                       #If PAT is missed
        print("Extra Point Missed!")            
    Kickoff(poss, userScore, oppScore)  