from random import randint
import os
def lin(x=60):
    print('='*x)
lines = '-'*50
lin()
print('MIND MATH GENIUS BUILDER GAME')
print(lines)
print("""At the and, only need to know the formules and algebric, geometric, functions... Combinatory, statistic, analytic geometry, analytic algebra.
You only need to do until the level 5~6. The level is less important than the test it'self.
Different from the previous game, this one is not easy, even using basic math, and excluding division.
The game it'self focus in develop the mental math instinct, the way the test is build is for this porpouse. Not to solve only.
The dificulty is base in memorization, how many test you need to memorized.
I use math, to not let you use visual memory, but imaginary visual memory, this is: you imagine the solution then store in you memory.""")
lin()
print("""# DOCUMENT GUIDE
# This programm is to Mental Math, not paper math. Do not write anything!\n# You can manipulate final result, is the only place you can modify is the result
# ALERT: YOU CANNOT HAVE -10 NEGATIVE POINT. That means 10 errors without right answer. Nor have level -1. 
# The common punity is regression of level, but you already will not out of level 0, that mean game over that is the maxim penauty, where the game close itself.
# The Level is the 10^Level. The size of the level is the power of 10.
# Only two wrong. But the point will value less as penauty and the wrong point will mutiply as a game, or you lose or win less if you repeat mistakens...
# Memory can't be anything different from int number or over 100. The game is flexible but everything have the down side or punity.""")
lin()
print('\n')
test = right = wrong = point = 0
try:
    level = int(input('Enter Level (0 as default): '))
except:
    level = 0

try:
    memory = int(input('Do you can memorized how many test? (not bigger than 120) '))
    if type(memory) != int or memory > 120:
        memory = 1
except:
    print('[Inválid] - Assuming 1 test!')
    memory = 1
lim = 120
while True:
    lista = []
    listc = []
    listSolutions = []
    listAnswers = []
    print(f"Level {level} | Point: {point} right: {right} Wrong: {wrong}\n{lines}\n")
    for i in range(memory):
        p1 = (10**(level))+8
        p2 = (10**(level+1))-1
        px = (p2+1)*2
        a = randint(2, p1)
        b = (randint(1, px)*5)/(p2+1)
        c = randint(2, p2)
        d = (randint(1, px)*5)/(p2+1)
        # main
        solution = (a*c)
        lista.append(a)
        listc.append(c)
        listSolutions.append(solution)
        listAnswers.append(0)
        print(f"({test}/{lim})\t| Test [{i}] = ({a-b: ^6.4g} + {b: ^6.4g}){'x': ^6.4}({c+d: ^6.4g} - {d:^6.4g})")
        # final
        test += 1
    # Question:
    #================================
    ask = input('\nSOLVED and Memorized?\n[ANY BUTTON TO CONTINUE...]')
    os.system('cls' if os.name == 'nt' else 'clear') 
    #================================
    xa = randint(2, p1)
    xb = (randint(1, px)*5)/(p2+1)
    xc = randint(2, p2)
    xd = (randint(1, px)*5)/(p2+1)
    x = xa*xc
    try:
        askx = int(input(f"Test [X] | ({xa-xb: ^6.4g} + {xb: ^6.4g}){'x': ^6.4}({xc+xd: ^6.4g} - {xd:^6.4g}) = "))
    except:
        askx = 0
    if askx == x:
        print('[✅] Right!')
    else:
        print('[❎] Wrong! - Answer: {x}')
    ask = input('\n\n[ANY BUTTON TO CONTINUE...]')
    os.system('cls' if os.name == 'nt' else 'clear') 
    #================================
    # this will garante that there have solve the problem without notating. To that, he need memorized the solution.
    lin()
    print('[TEST START!]')
    round = c = 0
    roundLimit = memory
    while round < roundLimit:
        if round != 0:
            print(f'\n{lines}\nMore {roundLimit-1} times [{round}/{roundLimit-1}]:\n{lines}\n')
            point
        for i in range(memory):
            try:
                answer = float(input(f"Test [{i}] = "))
            except:
                print('[INVALID ANSWER] - ONLY NUMBERS!')
                answer = 0
            listAnswers[i] = answer
        # Scan ListSolutions vs AnswersList 
        if listAnswers == listSolutions: # change by scan: True or False
            right += (1/(round+1))*memory
            point += (1/(round+1))*memory
            print(f'[✅] Right! (+{(1/(round+1))*memory} point)\n')
            break
        else:
            wrong += ((round+1)*memory)
            point -= ((round+1)*memory)
            # Rights numbers
            c = 0
            for i in range(memory):
                if listAnswers[i] == listSolutions[i]:
                    c += 1
            # print result
            print(f'[❎] Wrong! (-{(round+1)*memory} point) - Right Counter [{c}/{memory}]')
            round += 1
        if round < roundLimit:
            ask = input('Do you whant to repeat? (only if you remeber the answer!) [y/n] ')[0].lower()
            if ask == 'n':
                break
    if round == {roundLimit}:
        print('YOU LOSE YOU CHANCE!')
    print(f'Answer:\n')
    for i in range(memory):
        print(f"Test [{i}] =\t({lista[i]:^6.4g}{'x':^6.4}{listc[i]:^6.4g})\t= {listSolutions[i]:>6.4g} | You number: {listAnswers[i]:>6.4g}")
    print('='*50)
    ask = input('\n[ANY BUTTON TO CONTINUE...]')
    os.system('cls' if os.name == 'nt' else 'clear')
    #================================================
    if test > lim:
        res = str(input('Chose the level? [S/N] '))[0].lower()
        if res == 's':
            try:
                level = int(input('Enter Level (0 as default): '))
            except:
                level = 0
        else:
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
        
