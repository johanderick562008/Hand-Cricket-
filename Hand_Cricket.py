from random import*
from jdmod import*
 
num = list(range(0,11))
num1 = []

def youwontoss():
        print("You won the toss")
        while True:
            jd = user(str,"Batting or Bowling [X/Y]: ").upper()
            if jd in 'XY': break
            else: print("Invalid Character\n")
                
        if jd == 'X': jd= "Batting"
        elif jd == 'Y': jd= "Bowling"
        print("You chose",jd)
        global z,w
        z = 'uw'  # uw - you won
        w =jd        
def systemwontoss():
    print("System won the toss")
    jd1 =  choice(['Batting','Bowling'])
    print("System chose",jd1)
    global z,w1
    z = 'sw' # sw - system won
    w1 =jd1      
def youbatting():
    global num,x,y,jk,num1
    x = 0
    v = [8,9,10]
    v1 = [3,4,5]
    v2 = [6,7]
    while True:
        x1 = 0
        bt = user(int,"Enter : ")
  
        num1.append(bt)
        if len(num1)>=3:
                if num1[-1] == num1[-2]: 
                    bt1 = num1[-1]
                elif (num1[-1]==num1[-3] or num1[-1]== num1[-2]) and num1[-1] in v:
                        bt1 = choice(v)
                elif (num1[-1]==num1[-3] or num1[-1]== num1[-2]) and num1[-1] in v1:
                        bt1 = choice(v1)
                elif (num1[-1]==num1[-3] or num1[-1]== num1[-2]) and num1[-1] in v2:
                        bt1 = choice(v2)
                else:
                     bt1 = randint(0,10)        
        else:
              bt1 = randint(0,10)
        print("Your choice: ",bt)
        print("System choice:",bt1)
        if bt != bt1 and bt in num: x+=bt
        elif bt == 0: x+=bt1
        elif bt == bt1:
            print("\nBatsman out")
            break
        elif bt not in num:
            print("No ball due to inavlid character")
            print("Press 1 or 2 for next 3 balls")
            for i in range(3):
                bt2 = randint(1,2)
                nbl = None
                nbl = user(nbl,int,"Enter 1 or 2: ")
                print("Your choice: ",nbl)
                print("System choice:",bt2)
                if bt2 == nbl :
                        if x1 == 0: x1+=1
                        elif x1 == 1:
                             print("\nBatsman out")
                             x1+=1
                             break
            
                elif nbl not in [1,2]:
                    print("\nBatsman out due to invalid character")
                    x1+=1
                    break
                elif bt2 != nbl and nbl in [1,2]:pass            
        if x1==2: break
        if x>y: break
    jk = x    
    
        
def systembatting():
    global num,y,x,jk1
    y = 0
    while True:
        bt = user(int,"Enter: ")  
        bt1 = randint(0,10)
        print("Your choice: ",bt)
        print("System choice:",bt1)
        if bt != bt1 : y+=bt1
        elif bt1 == 0: y+=bt
        elif bt1 == bt:
            print("\nBatsman out")
            break
        elif bt not in num:y+=10
        if y>x:break
    jk1 = y
    
def trails():
        k = user(int,"Enter a number between 0 to 10 (Trails): ")
        l = randint(0,10)
        print("Your choice: ",k)
        print("System choice:",l,'\n')
def youbat():
    print("\nYou are batting")
    print("System is bowling\n")
def sysbat():
    print("\nYou are bowling")
    print("System is battng\n")
    
print("TOSS")
print("1.Heads or Tails")
print("2.Odd or Even")




while True:
    a = user(int,"Enter your choice for TOSS [1/2]: ")
    if a in [1,2]: break
    else: print("Invalid Character\n")
        

if a == 1: # Head or Tail

    
    while True:
        b = user(str,"Heads or Tails [H/T]: ").upper()
        if b in 'HT': break
        else: print("Invalid Character\n")
    c = choice(['H','T'])
    if b == c: youwontoss()   
    elif b!=c and b in 'HT' :systemwontoss()  

elif a == 2: # Odd or Even

    
    while True:
        e = user(str,"Odd or Even [O/E]: ").upper()
        if e in 'OE': break
        else: print("Invalid Character\n")
    g = user(int,"Enter a number from 0 to 10: ") 
    h = randint(0,10)
    print("Your choice: ",g)
    print("System choice:",h)
    if (g+h)%2==0: i = 'E'
    else: i = 'O'
    if i == e:youwontoss()
    elif i!=e and e in 'OE' :systemwontoss()
    

print("Let's go....")
wait(2)
rules = ["\nFor Batting: ",
         '1) Enter a number from 0 to 10',
         '2) If the scores are equal, the batsman is out',
         '3)If the scores are not equal, the batsman score is added to the batting teams total runs',
         '4)Ivalid characters are no ball',
         '5) No ball means batsman should play with 1 or 2 for 3 times',
         '6) Play with other numbers or 2 times during out is out '
         '7) Keeping 0, bowlers score is batsman score',' ',
         "For Bowling: ",
         '1) Enter a number from 0 to 10',
         '2) If the scores are equal, the batsman is out',
         '3)If the scores are not equal, the batsman score is added to the batting teams total runs',
         '4)Ivalid characters are no ball',
         '5)No ball means 10 runs for batsman',
         '6) Keeping 0, bowlers score is batsman score\n',
         ]
for i in rules:
    for j in i:
        wait(0.001)
        print(j,end='')
    print()        
            
wait(2)    
print("\nFirst innings")
t = 0
if z == 'uw':
    if w == "Batting":
        y=10**100000 
        t=1
        youbat()
        trails()
        youbatting()
        print("Your Total: ",x)
        print('System Target:',x+1)
       
    elif w == "Bowling":
        x=10**100000 
        t=2
        sysbat()
        trails()
        systembatting()
        print("System Total: ",y)
        print('Your Target:',y+1)
        
elif z == 'sw':
    if w1 == "Batting":
        t=2
        x=10**100000 
        sysbat()
        trails()
        systembatting()
        print("System Total: ",y)
        print('Your Target:',y+1)
    elif w1 == "Bowling":
        t=1
        y=10**100000 
        youbat()
        trails()
        youbatting()
        print("Your Total: ",x)
        print('System Target:',x+1)
x = 0
y = 0
wait(2)
print("\nSecond innings")

if t == 1:
        x=jk
        sysbat()
        trails()
        systembatting()
        print("System Total: ",y)
        if y > x :print("System won")
        elif y < x :print("You Won!!")
        elif y==x:print("Match Tied")

elif t == 2:
        y=jk1
        youbat()
        trails()
        youbatting()
        print("Your Total: ",x)
        if y > x :print("System won")
        elif y < x :print("You won")
        elif y==x:print("Match Tied")


