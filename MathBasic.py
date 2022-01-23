from random import randint
import os
def lin(x=30):
    print('='*x)
lin()
print("""# ALERT: YOU CANNOT HAVE -10 NEGATIVE POINT. That means 10 errors without right answer.
# Good luck! Strengh, yes!, you can do it! Please, only 100 minimal test!
# You don't need to do all the 1000 thausand, 100 is enough to prove youself. But, 1000 will garantee youself!
""")
lin()
print('\n')
test = right = wrong = point = 0
level = int(input('Enter Level (0 as default): '))
lim = 1000
while True:
    p = (10**(level+1))-1
    pLevel = ((p+1)*10)-1
    a = randint(2, p)/10
    b = (randint(2, p)/100)
    if b == 1:
        b += (randint(2, pLevel)/100)
    lin(80)
    solution = ((((a*100))*(b*100))/10**4) # treat the solution | Memory erro that make a bug of ...9999999... The solution have been put all in interger.
    print(f"Level {level}, test: ({test}/{lim}) \t| Point: {point:.4g} \t| Right: {right} \tWrong: {wrong} |\n{'-'*80}\n({a} x {b}) = [First Solution]")
    print('')
    #================================
    ask = input('\nSOLVED and Memorized?\n[ENTER TO CONTINUE...]')
    os.system('cls' if os.name == 'nt' else 'clear') 
    #================================
    while True:
        answer = float(input('[Final Solution] = '))
        try:
            if answer == solution:
                right += 1
                point += 1
                print(f'[✅] Right! - [+1]')
            else:
                wrong += 1
                point -= 1
                print(f'[❎] Wrong! - [-1]')
            break
        except:
            print('Invalid Answer!')
    #================================
    #================================
    print(f'\nAnswer:\t({a} x {b}) = {solution}')
    lin(80)
    #================================
    ask = input('\n[ENTER TO CONTINUE...]')
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
        
