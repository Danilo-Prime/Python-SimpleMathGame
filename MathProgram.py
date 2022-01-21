from random import randint
import os
def lin(x=30):
    print('='*x)
lin()
print("""# ALERT: YOU CANNOT HAVE -10 NEGATIVE POINT. That means 10 errors without right answer.
# The Level is the 10^Level. The size of the level is the power of 10.
# Limit of 4 digit of decimals.
""")
lin()
print('\n')
test = right = wrong = point = 0
level = int(input('Enter Level (0 as default): '))
lim = 1000
while True:
    p = (10**(level+1))-1
    px = (10**(level+2))-1
    a = randint(2, p)/100
    b = (randint(2, px))/(p+1)
    if b == 1:
        b += (randint(2, px))/(p+1)
    n1 = (randint(2, 999))
    n2 = (randint(2, 999))
    lin(80)
    solution = (((a*1000)*(b*1000))/10**6) # treat the solution | Memory erro that make a bug of ...9999999... The solution have been put all in interger.
    print(f"Level {level}, test: ({test}/{lim}) \t| Point: {point} \t| Right: {right} \tWrong: {wrong} |\n{'-'*80}\n({a} x {b}) = [First Solution]")
    print('')
    #================================
    ask = input('\nSOLVED and Memorized?\n[ENTER TO CONTINUE...]')
    os.system('cls' if os.name == 'nt' else 'clear') 
    #================================
    pPoint = 0
    for i in range(3):
        n3 = (randint(2, 9999))
        n4 = (randint(2, 9999))
        nA = (n1-n2)
        nB = (n3-n4)
        nX = ((nA+nB)*10**i)/1000
        answer2 = float(input(f"[Sum Test {i+1}/3 for Pass Through]\n({(nA*10**i)/1000} + {(nB*10**i)/1000}) = "))
        if answer2 == nX:
            print('[✅] Right!')
            pPoint += 1
        else:
            print('[❎] Wrong!')
            print(f'[Answer]: {nX}')
        print('')
    #================================
    ask = input('\nSOLVED and Memorized?\n[ENTER TO CONTINUE...]')
    os.system('cls' if os.name == 'nt' else 'clear') 
    #================================
    answer = float(input('[Final Solution] = '))
    if answer == solution:
        right += 1
        pPoint += 3
        point += (1/6)*pPoint
        print(f'[✅] Right! - [+{(1/6)*pPoint}]')
    else:
        wrong += 1
        point -= (1/(pPoint+1))
        print(f'[❎] Wrong! - [-{(1/(pPoint+1))}]')
    #================================
    #================================
    print(f'\nAnswer:\n({a} x {b}) = {solution}')
    lin(80)
    #================================
    ask = input('\nSOLVED and Memorized?\n[ENTER TO CONTINUE...]')
    os.system('cls' if os.name == 'nt' else 'clear') 
    #================================
    test += 1
    if test > lim:
        if point > lim*0.66:
            level += 1
            test = 0
            point = 0
            print(f'[🏆] 🎈 Congratulations! 🎉 - You have been upgrade of level.\n |LEVEL {level} |')
        else:
            print('Level Over! - Restarting Level')
            test = 0
            point = 0
        
    if point == -10:
        print('Low point!\nRegressing Level')
        level -= 1
        test = 0
    if level == -1:
        print('You need learn MATH FIRST! You loose in the first level. This is END GAME!')
        print('Game Over.')
        break
    print('')
        
